import urllib2
import json
import logging
from colab.plugins.data import PluginDataImporter
from colab_taiga.models import TaigaProject, TaigaUser, TaigaUserStory


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

                project_owner = TaigaUser.objects.get(pk=json_project['owner']['id'])

                project = TaigaProject.objects.get_or_create(
                    id=json_project['id'], owner=project_owner)[0]

                project.title = json_project['name']
                project.description = json_project['description']
                project.slug = json_project['slug']
                try:
                    members = TaigaUser.objects.filter(
                        id__in=json_project['members'])
                    for member in members:
                        project.users.add(member)
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

    def fetch_user_stories(self):
        next_page = self.build_url('/api/v1/userstories')

        while next_page:
            json_data, next_page = self.get_data(next_page)
            for json_user_story in json_data:
                user_story_project = TaigaProject.objects.get(
                    pk=json_user_story['project'])
                if json_user_story['assigned_to']:
                    user_story_assigned_to = TaigaUser.objects.get(
                        pk=json_user_story['assigned_to'])
                user_story = TaigaUserStory.objects.get_or_create(
                    id=json_user_story["id"], project=user_story_project,
                    assigned_to=user_story_assigned_to)[0]
                user_story.subject = json_user_story['subject']
                user_story.total_points = json_user_story['total_points']
                user_story.milestone = json_user_story['milestone']
                user_story.is_closed = json_user_story['is_closed']
                try:
                    user_story.save()
                except:
                    LOGGER.exception('Failed to import user_story with id=%s' %
                                     json_user_story["id"])
                    continue

    def fetch_data(self):
        LOGGER.info('Importing Taiga data')
        LOGGER.info('Importing Projects...')
        self.fetch_users()
        self.fetch_projects()
        self.fetch_user_stories()

        LOGGER.info('Data imported')
