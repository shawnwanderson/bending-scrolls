from django.conf.urls import include, url
from django.contrib import admin
from scrolls import views

urlpatterns = [
    url(r'^$', views.ScrollListView, name='scrolls'),
    url(r'^(?P<scroll_id>[0-9]+)/$', views.ScrollDetailView, name='scroll'),
]
