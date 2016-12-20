from django.conf.urls import include, url
from django.contrib import admin
from scrolls import views
from scrolls import urls as scrolls_urls

urlpatterns = [
    url(r'^$', views.QueryView.as_view(), name='index'),
    url(r'^scrolls/', include(scrolls_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
]
