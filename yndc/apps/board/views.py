from django import forms
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from board.models import Board, House, Neighborhood
from board.forms import BoardForm, HouseForm, NeighborhoodForm


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('list'))
    else:
        form = AuthenticationForm()
    return render(request, 'board/login.html', {'form': form})


@login_required()
def list(request):
    ctx = {'page': 'properties'}

    houses = House.objects.active()

    if request.GET.get('neighborhood'):
        try:
            neighborhood_filter = Neighborhood.objects.get(slug=request.GET['neighborhood'])
        except Neighborhood.DoesNotExist:
            pass
        else:
            ctx['neighborhood_filter'] = neighborhood_filter
            houses = houses.filter(neighborhood_id=neighborhood_filter.pk)

    ctx['houses'] = houses
    ctx['neighborhoods'] = Neighborhood.objects.all()
    return render(request, 'board/list.html', ctx)


@login_required
def house(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)
    return render(request, 'board/house.html', {'house': house})


@login_required
def archive_house(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)
    house.archived = True
    house.save()
    return HttpResponseRedirect(reverse('list'))


@login_required
def add_house(request):
    widgets = {
        'height': forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'height'}),
        'width': forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'width'}),
        'description': forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'description'})
    }

    BoardFormSet = modelformset_factory(Board, form=BoardForm, extra=2,
        widgets=widgets)

    if request.method == 'POST':
        house_form = HouseForm(request.POST, request.FILES)
        board_formset = BoardFormSet(request.POST, queryset=Board.objects.none())

        if house_form.is_valid() and board_formset.is_valid():
            house = house_form.save()
            boards = board_formset.save(commit=False)
            for board in boards:
                board.house = house
                board.save()
            return HttpResponseRedirect(reverse('house', args=[house.slug]))
    else:
        house_form = HouseForm()
        board_formset = BoardFormSet(queryset=Board.objects.none())

    return render(request, 'board/add_house.html',
        {'house_form': house_form, 'board_formset': board_formset})

@login_required
def neighborhoods(request):
    return render(request, 'board/neighborhoods.html',
        {'neighborhoods': Neighborhood.objects.all(), 'page': 'neighborhoods'})


@login_required
def add_neighborhood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('neighborhoods'))
    else:
        form = NeighborhoodForm()

    return render(request, 'board/add_neighborhood.html',
        {'form': form})


@login_required
def delete_neighborhood(request, neighborhood_slug):
    neighborhood = get_object_or_404(Neighborhood, slug=neighborhood_slug)
    neighborhood.delete()
    return HttpResponseRedirect(reverse('neighborhoods'))
