from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.current_cats),
    url(r'^kitty/(?P<pk>[0-9]+)/$', views.cat_detail),
]
