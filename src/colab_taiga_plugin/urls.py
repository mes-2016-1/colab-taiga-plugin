
from django.conf.urls import patterns, url

from .views import ColabTaigaPluginProxyView

urlpatterns = patterns('',
    url(r'^(?P<path>.*)$', ColabTaigaPluginProxyView.as_view(),
        name='colab_taiga_plugin'),
)
