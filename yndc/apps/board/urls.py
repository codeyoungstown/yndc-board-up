from django.conf.urls import patterns, url

urlpatterns = patterns('board.views',
    url(r'^/?$', 'list', name='list'),
    url(r'^add-property/?$', 'add_house', name='add_house'),
    url(r'^property/(?P<house_slug>[\w-]+)/?$', 'house', name='house'),
    url(r'^property/(?P<house_slug>[\w-]+)/archive/?$', 'archive_house', name='archive_house'),
    url(r'^neighborhoods/?$', 'neighborhoods', name='neighborhoods'),
    url(r'^neighborhoods/add-neighborhood/?$', 'add_neighborhood', name='add_neighborhood'),
    url(r'^neighborhoods/(?P<neighborhood_slug>[\w-]+)/delete/?$', 'delete_neighborhood', name='delete_neighborhood'),
    url(r'^login/?$', 'login_user'),
)
