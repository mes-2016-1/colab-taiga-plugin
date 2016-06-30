
from colab.plugins.utils.apps import ColabPluginAppConfig


class TaigaPluginAppConfig(ColabPluginAppConfig):
    name = 'colab_taiga'
    verbose_name = 'Taiga Plugin'
    short_name = 'taiga'
    namespace = 'taiga'

    def ready(self):
        from . import signals  # noqa
        super(TaigaPluginAppConfig, self).ready()
