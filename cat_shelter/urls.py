from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.current_cats),
    url(r'^kitty/(?P<pk>[0-9]+)/$', views.cat_detail),
    url(r'^cat/new/$', views.cat_new, name='cat_new'),
    url(r'^cat/(?P<pk>[0-9]+)/edit/$', views.cat_edit, name='cat_edit'),
]
