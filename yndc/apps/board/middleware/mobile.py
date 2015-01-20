import re

RE_MOBILE = re.compile(r"android|ip(hone|od|ad)", re.I|re.M)


class MobileMiddleware(object):
    def process_request(self, request):
        request.is_mobile = False
        if request.META.get('HTTP_USER_AGENT'):
            if re.search(RE_MOBILE, request.META['HTTP_USER_AGENT']):
                request.is_mobile = True
