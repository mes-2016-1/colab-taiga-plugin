
from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_taiga'
verbose_name = 'Taiga Plugin'

upstream = 'localhost'
# middlewares = []

urls = {
    'include': 'colab_taiga.urls',
    'prefix': '^taiga/',
}

menu_title = _('taiga')

url = colab_url_factory('taiga')

# Extra data to be exposed to plugin app config
extra = {}

menu_urls = (
    url(display=_('Dashboard'), viewname='taiga',
        kwargs={'path': ''}, auth=False),
    url(display=_('My Projects'), viewname='taiga',
        kwargs={'path': 'projects'}, auth=True),
    url(display=_('Profile'), viewname='taiga',
        kwargs={'path': 'profile'}, auth=True),
)
