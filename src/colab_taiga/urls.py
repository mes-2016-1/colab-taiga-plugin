
from django.conf.urls import patterns, url

from .views import TaigaPluginProxyView

urlpatterns = patterns('',
                       url(r'^(?P<path>.*)$', TaigaPluginProxyView.as_view(),
                           name='taiga'))
