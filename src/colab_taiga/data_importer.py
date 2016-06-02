
from colab.plugins.data import PluginDataImporter


class ColabTaigaPluginDataImporter(PluginDataImporter):
    app_label = 'colab_taiga'

    def fetch_data(self):
        pass
