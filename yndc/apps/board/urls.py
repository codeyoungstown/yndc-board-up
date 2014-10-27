from django.conf.urls import patterns, url

urlpatterns = patterns('board.views',
    url(r'^/?$', 'list', name='list'),
    url(r'^add/?$', 'add_house', name='add'),
    url(r'^neighborhood/(?P<neighborhood_slug>[\w_]+)/?$', 'neighborhood'),
    url(r'^house/(?P<house_slug>[\w-]+)/?$', 'house', name='house'),
    url(r'^login/?$', 'login_user'),
)
