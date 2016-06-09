import urllib2
import json

from colab.plugins.data import PluginDataImporter

from colab_taiga.models import TaigaProject


class TaigaPluginDataImporter(PluginDataImporter):
    app_label = 'colab_taiga'

    def build_url(self, endpoint):
        upstream = self.config.get('upstream')
        return "%s%s" % (upstream, endpoint)

    def get_data(self, url):
        try:
            response = urllib2.urlopen(url, timeout=1000)
            json_data = json.load(response)
            next_page = response.info().getheader('X-Pagination-Next')
        except urllib2.URLError:
            json_data = {}
            next_page = None

        return json_data, next_page

    def fetch_projects(self):
        next_page = self.build_url('/api/v1/projects')

        while next_page:
            json_data, next_page = self.get_data(next_page)
            for json_project in json_data:
                project = TaigaProject()
                project.title = json_project['name']
                project.description = json_project['description']
                try:
                    project.save()
                except:
                    continue


    def fetch_data(self):
        self.fetch_projects()

