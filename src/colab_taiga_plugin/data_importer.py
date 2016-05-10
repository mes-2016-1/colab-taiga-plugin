
from colab.plugins.data import PluginDataImporter


class ColabTaigaPluginDataImporter(PluginDataImporter):
    app_label = 'colab_taiga_plugin'

    def fetch_data(self):
        pass
