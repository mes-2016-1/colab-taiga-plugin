
from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_taiga'
verbose_name = 'Taiga Plugin'

upstream = 'localhost'
# middlewares = []

urls = {
    'include': 'colab_taiga.urls',
    'prefix': '^colab_taiga/',
}

menu_title = _('taiga')

url = colab_url_factory('taiga')

# Extra data to be exposed to plugin app config
extra = {}

menu_urls = (
# Example of menu URL:
#    url(display=_('Public Projects'), viewname='colab_taiga_plugin',
#        kwargs={'path': 'public/projects'}, auth=False),

# Example of authenticated user menu URL:
#    url(display=_('Profile'), viewname='colab_taiga_plugin',
#        kwargs={'path': 'profile'}, auth=True),
)
