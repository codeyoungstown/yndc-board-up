from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from board.models import Board, House, Neighborhood
from board.forms import BoardForm, HouseForm


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('list'))
    else:
        form = AuthenticationForm()
    return render_to_response('board/login.html', {'form': form},
        context_instance=RequestContext(request))


@login_required()
def list(request):
    houses = House.objects.all()
    return render_to_response('board/list.html', {'houses': houses,
        'page': 'properties'}, context_instance=RequestContext(request))


@login_required
def neighborhood(request, neighborhood_slug):
    neighborhood = get_object_or_404(Neighborhood, slug=neighborhood_slug)
    houses = House.objects.filter(neighborhood_id=neighborhood.pk)
    return render_to_response('board/neighborhood.html',
        {'neighborhood': neighborhood, 'houses': houses,
        'page': 'neighborhoods'}, context_instance=RequestContext(request))


@login_required
def house(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)
    return render_to_response('board/house.html', {'house': house},
        context_instance=RequestContext(request))


@login_required
def add_house(request):
    BoardFormSet = modelformset_factory(Board, form=BoardForm, extra=2)

    if request.method == 'POST':
        house_form = HouseForm(request.POST)
        board_formset = BoardFormSet(request.POST)

        if house_form.is_valid() and board_formset.is_valid():
            house = house_form.save()
            boards = board_formset.save(commit=False)
            for board in boards:
                board.house = house
                board.save()
            return HttpResponseRedirect(reverse('house', args=[house.slug]))
    else:
        house_form = HouseForm()
        board_formset = BoardFormSet()

    return render_to_response('board/add_house.html',
        {'house_form': house_form, 'board_formset': board_formset},
        context_instance=RequestContext(request))
