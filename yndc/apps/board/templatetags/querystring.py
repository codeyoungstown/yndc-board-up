import re
import urllib

from django import template
from django.template.base import Node


register = template.Library()


# Regex for token keyword arguments

kwarg_re = re.compile(r"(?:(\w+\[?\]?\+?\-?)=)?(.+)")


def token_kwargs(bits, parser, support_legacy=False):
    
    """
    This is an exact copy of django.template.defaulttags.token_kwargs but
    with kwarg_re modified to accept params with brackets, like {% sometag hey[]='yo' %},
    and add/remove mofidiers, like {% sometag hey[]+='dude' %}
    """

    if not bits:
        return {}
    match = kwarg_re.match(bits[0])
    kwarg_format = match and match.group(1)
    if not kwarg_format:
        if not support_legacy:
            return {}
        if len(bits) < 3 or bits[1] != 'as':
            return {}

    kwargs = {}
    while bits:
        if kwarg_format: 
            match = kwarg_re.match(bits[0])
            if not match or not match.group(1):
                return kwargs
            key, value = match.groups()
            del bits[:1]
        else:
            if len(bits) < 3 or bits[1] != 'as':
                return kwargs
            key, value = bits[2], bits[0]
            del bits[:3]
        kwargs[key] = parser.compile_filter(value)
        if bits and not kwarg_format:
            if bits[0] != 'and':
                return kwargs
            del bits[:1]
    return kwargs

class QueryStringNode(Node):

    """
    Handle querystring tag parsing
    """

    def __init__(self, query_string, arguments={}, append=False):

        """
        Query string init

            `query_string`  (dict)  The variable containing the original query string we are analyzing/modifying
            `arguments`     (dict)  Token arguments dictionary -- variable names to be replaced with specified values
            `append`        (bool)  Boolean to determine whether the resulting query string starts with a '?' or a '&'

        """
        self.query_string_var = query_string
        self.query_string_data = template.Variable(self.query_string_var)
        self.arguments = arguments
        self.append = append

    def render(self, context):

        """
        Render query string
        """

        from copy import deepcopy

        # Grab query string context var
        try:
            query_string_data = deepcopy(self.query_string_data.resolve(context))
            if type(query_string_data) != dict:
                raise Exception()
        except Exception:
            # Default to an empty query string dict
            query_string_data = {}

        # Sort through arguments and update query string data accordingly

        if self.arguments:
            for var, filter_expression in self.arguments.items():
                value = filter_expression.resolve(context, True)
                append = var[-1] == '+'
                remove = var[-1] == '-'
                if append or remove: var = var[0:-1]

                if query_string_data.has_key(var):
                    if type(query_string_data[var]) is list and (append or remove):
                        if remove:
                            try:
                                ind = query_string_data[var].index(value)
                                del query_string_data[var][ind]
                            except:
                                pass
                        else:
                            query_string_data[var].append(value)
                    elif value == None:
                        del query_string_data[var]
                    #elif value:
                    #   query_string_data[var] = value
                    else:
                        query_string_data[var] = value
                elif value:
                    query_string_data[var] = [value] if append else value

        # Preparse for encoding
        query_string_data_list = []

        for key in query_string_data.keys():
            value = query_string_data[key]
            if type(value) in [list, tuple]:
                key = str(key)
                for item in value:
                    query_string_data_list.append((key, str(item),))
            else:
                query_string_data_list.append((key, str(value),))

        # Build and return query string

        if query_string_data:
            return '%s%s' % ('&' if self.append else '?', urllib.urlencode(query_string_data_list))
        else:
            return ''


@register.tag(name='querystring')
def do_querystring(parser, token):

    """
    Query string tag: use a base query string dictionary, pass in arguments to replace particular query string variables.
    Returns a parsed out query string with the variables, like: ?foo=bar&filter=date

    Usage:

        base_query_string = {'foo': 'bar'}
        {% querystring base_query_string %}
        '?foo=bar'

        base_query_string = {'foo': 'bar', 'dude': 'hello'}
        {% querystring base_query_string %}
        '?foo=bar&dude=hello'

        base_query_string = {'foo': 'bar', 'dude': 'hello'}
        {% querystring base_query_string dude='smelly' %}
        '?foo=bar&dude=smelly'

    Pass 'append' keyword as the last argument for the query string to start with a '&' instead of a '?'

    See tests.py for more examples

    """

    bits = token.split_contents()
    arguments = {}
    append = False

    # Get base query string dict

    try:
        query_string_data = bits[1]
    except:
        raise template.TemplateSyntaxError('%s tag requires at least one argument: a base query string dictionary')

    # Check for arguments

    remaining_bits = bits[2:]

    if remaining_bits:

        # Check for 'append'

        if 'append' in remaining_bits:
            append = True
            remaining_bits.remove('append')

        # Parse remaining arguments

        try:
            arguments = token_kwargs(remaining_bits, parser)
        except:
            arguments = {}

    return QueryStringNode(query_string_data, arguments, append)
