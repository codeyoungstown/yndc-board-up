from django.conf.urls import url

from board import views as board_views

urlpatterns = [
    url(r'^/?$', board_views.list, name='list'),
    url(r'^bulk-print/?$', board_views.bulk_print, name='bulk_print'),
    url(r'^add-property/?$', board_views.add_house, name='add_house'),
    url(r'^property/(?P<house_slug>[\w-]+)/?$', board_views.house, name='house'),
    url(r'^property/(?P<house_slug>[\w-]+)/edit/?$', board_views.edit_house, name='edit_house'),
    url(r'^property/(?P<house_slug>[\w-]+)/delete/?$', board_views.delete_house, name='delete_house'),
    url(r'^property/(?P<house_slug>[\w-]+)/archive/?$', board_views.archive_house, name='archive_house'),
    url(r'^property/(?P<house_slug>[\w-]+)/unarchive/?$', board_views.unarchive_house, name='unarchive_house'),
    url(r'^property/(?P<house_slug>[\w-]+)/print/?$', board_views.print_house, name='print_house'),
    url(r'^property/(?P<house_slug>[\w-]+)/boards/?$', board_views.boards, name='boards'),
    url(r'^property/(?P<house_slug>[\w-]+)/boards/add/?$', board_views.add_board, name='add_board'),
    url(r'^property/(?P<house_slug>[\w-]+)/boards/(?P<board_id>\d+)/edit/?$', board_views.edit_board, name='edit_board'),
    url(r'^property/(?P<house_slug>[\w-]+)/boards/(?P<board_id>\d+)/delete/?$', board_views.delete_board, name='delete_board'),
    url(r'^property/(?P<house_slug>[\w-]+)/events/?$', board_views.events, name='events'),
    url(r'^property/(?P<house_slug>[\w-]+)/events/add/?$', board_views.add_event, name='add_event'),
    url(r'^property/(?P<house_slug>[\w-]+)/events/(?P<event_id>\d+)/?$', board_views.event, name='event'),
    url(r'^property/(?P<house_slug>[\w-]+)/events/(?P<event_id>\d+)/archive/?$', board_views.archive_event, name='archive_event'),
    url(r'^property/(?P<house_slug>[\w-]+)/events/(?P<event_id>\d+)/edit/?$', board_views.edit_event, name='edit_event'),
    url(r'^neighborhoods/?$', board_views.neighborhoods, name='neighborhoods'),
    url(r'^neighborhoods/add-neighborhood/?$', board_views.add_neighborhood, name='add_neighborhood'),
    url(r'^neighborhoods/(?P<neighborhood_slug>[\w-]+)/delete/?$', board_views.delete_neighborhood, name='delete_neighborhood'),
    url(r'^login/?$', board_views.login_user),
    url(r'^logout/?$', board_views.logout_user, name='logout_user'),
]
