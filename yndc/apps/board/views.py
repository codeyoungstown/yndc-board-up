from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render

from board.models import Board, Event, House, Neighborhood
from board.forms import BoardForm, EventForm, HouseForm, NeighborhoodForm


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('list'))
    else:
        form = AuthenticationForm()
    return render(request, 'board/login.html', {'form': form})


def logout_user(request):
    if not request.user.is_authenticated():
        raise Http404()

    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


@login_required()
def list(request):
    ctx = {'page': 'properties'}

    houses_queryset = House.objects

    # Archived filter
    if request.GET.get('archived') == '1':
        ctx['archived_filter'] = True
        houses_queryset = houses_queryset.filter(archived=True)
    else:
        houses_queryset = houses_queryset.active()

    # Search
    search_query = request.GET.get('search')
    if search_query:
        ctx['search_query'] = search_query
        houses_queryset = houses_queryset.filter(address__contains=search_query)

    # Neighborhood filter
    if request.GET.get('neighborhood'):
        try:
            neighborhood_filter = Neighborhood.objects.get(slug=request.GET['neighborhood'])
        except Neighborhood.DoesNotExist:
            pass
        else:
            ctx['neighborhood_filter'] = neighborhood_filter
            houses_queryset = houses_queryset.filter(neighborhood_id=neighborhood_filter.pk)

    paginator = Paginator(houses_queryset, 50)
    page = request.GET.get('page')

    try:
        houses = paginator.page(page)
    except PageNotAnInteger:
        houses = paginator.page(1)
    except EmptyPage:
        houses = paginator.page(paginator.num_pages)

    ctx['houses'] = houses
    ctx['neighborhoods'] = Neighborhood.objects.all()
    ctx['query_string'] = dict(request.GET)
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
def unarchive_house(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)
    house.archived = False
    house.save()
    return HttpResponseRedirect(reverse('list'))


@login_required
def delete_house(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)
    house.delete()
    return HttpResponseRedirect(reverse('list'))


@login_required
def add_house(request):
    if request.method == 'POST':
        house_form = HouseForm(request.POST, request.FILES)

        if house_form.is_valid():
            house = house_form.save(commit=False)
            house.created_by = request.user
            house.save()
            return HttpResponseRedirect(reverse('house', args=[house.slug]))
    else:
        house_form = HouseForm()

    return render(request, 'board/add_house.html',
        {'house_form': house_form})


@login_required
def edit_house(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)

    if request.method == 'POST':
        house_form = HouseForm(request.POST, request.FILES, instance=house)

        if house_form.is_valid():
            house = house_form.save(commit=False)
            house.created_by = request.user
            house.save()
            return HttpResponseRedirect(reverse('house', args=[house.slug]))
    else:
        house_form = HouseForm(instance=house)

    return render(request, 'board/add_house.html',
        {'house_form': house_form})


@login_required
def print_house(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)
    return render(request, 'board/print.html', {'houses': [house]})


@login_required
def bulk_print(request):
    house_pks = request.GET.getlist('houses')
    houses = House.objects.filter(pk__in=house_pks)
    return render(request, 'board/print.html', {'houses': houses})


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


@login_required
def boards(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)
    return render(request, 'board/boards.html', {'house': house})


@login_required
def add_board(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)

    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.save(commit=False)
            board.house = house
            board.save()
            return HttpResponseRedirect(reverse('boards', args=[house_slug]))
    else:
        form = BoardForm()

    return render(request, 'board/add_board.html', {'house': house,
        'form': form})


@login_required
def edit_board(request, house_slug, board_id):
    try:
        board = Board.objects.select_related('house').get(pk=board_id,
            house__slug=house_slug)
    except:
        raise Http404()

    if request.method == 'POST':
        board_form = BoardForm(request.POST, instance=board)

        if board_form.is_valid():
            board.save()
            return HttpResponseRedirect(reverse('boards', args=[board.house.slug]))
    else:
        board_form = BoardForm(instance=board)

    return render(request, 'board/add_board.html', {'house': board.house,
        'form': board_form})


@login_required
def delete_board(request, house_slug, board_id):
    board = get_object_or_404(Board, house__slug=house_slug, pk=board_id)
    board.delete()
    return HttpResponseRedirect(reverse('boards', args=[house_slug]))


@login_required
def events(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)
    return render(request, 'board/events.html', {'house': house})


@login_required
def event(request, house_slug, event_id):
    event = get_object_or_404(Event, house__slug=house_slug, pk=event_id)
    return render(request, 'board/event.html', {'event': event})


@login_required
def add_event(request, house_slug):
    house = get_object_or_404(House, slug=house_slug)

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.house = house
            event.created_by = request.user
            event.save()
            return HttpResponseRedirect(reverse('events', args=[house_slug]))
    else:
        form = EventForm()

    return render(request, 'board/add_event.html', {'house': house,
        'form': form})


@login_required
def archive_event(request, house_slug, event_id):
    event = get_object_or_404(Event, house__slug=house_slug, pk=event_id)
    event.archived = True
    event.save()
    return HttpResponseRedirect(reverse('events', args=[house_slug]))


@login_required
def edit_event(request, house_slug, event_id):
    event = get_object_or_404(Event, house__slug=house_slug, pk=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('events', args=[house_slug]))
    else:
        form = EventForm(instance=event)

    return render(request, 'board/add_event.html', {'house': event.house,
        'form': form})
