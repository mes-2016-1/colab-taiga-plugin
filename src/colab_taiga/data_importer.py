import urllib2
import json
import logging

from colab.plugins.data import PluginDataImporter

from colab_taiga.models import TaigaProject, TaigaUser


LOGGER = logging.getLogger('colab_taiga')

class TaigaPluginDataImporter(PluginDataImporter):
    app_label = 'colab_taiga'

    def build_url(self, endpoint):
        upstream = self.config.get('upstream')
        return "%s%s" % (upstream, endpoint)

    def get_data(self, url):
        try:
            response = urllib2.urlopen(url, timeout=10)
            json_data = json.load(response)
            next_page = response.info().getheader('X-Pagination-Next')
        except urllib2.URLError:
            LOGGER.exception('Failed to connect to Taiga API')
            json_data = {}
            next_page = None

        return json_data, next_page

    def fetch_projects(self):
        next_page = self.build_url('/api/v1/projects')

        while next_page:
            json_data, next_page = self.get_data(next_page)
            for json_project in json_data:
                project = TaigaProject.objects.get_or_create(
                    id=json_project["id"])[0]
                project.title = json_project['name']
                project.description = json_project['description']
                try:
                    project.save()
                except:
                    LOGGER.exception('Failed to import project with id=%s' %
                                     json_project["id"])
                    continue

    def fetch_users(self):
        next_page = self.build_url('/api/v1/users')

        while next_page:
            json_data, next_page = self.get_data(next_page)
            for json_user in json_data:
                user = TaigaUser.objects.get_or_create(
                    id=json_user["id"])[0]
                user.username = json_user['username']
                user.full_name = json_user['full_name']
                user.bio = json_user['bio']
                user.is_active = json_user['is_active']
                try:
                    user.save()
                except:
                    LOGGER.exception('Failed to import user with id=%s' %
                                     json_user["id"])
                    continue


    def fetch_data(self):
        LOGGER.info('Importing Taiga data')
        LOGGER.info('Importing Projects...')
        self.fetch_users()
        self.fetch_projects()

        LOGGER.info('Data imported')
