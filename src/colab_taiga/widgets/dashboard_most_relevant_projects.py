from colab.widgets.widget_manager import Widget
from colab_taiga.models import TaigaProject, TaigaUser


class DashboardMostRelevantProjectsWidget(Widget):
    name = 'most relevant projects'
    template = 'widgets/dashboard_most_relevant_projects.html'

    def generate_content(self, **kwargs):
        projects = []

        if kwargs['context']['user'].is_authenticated():
            logged_colab_user = kwargs['context']['user']
            logged_taiga_user = TaigaUser.objects.filter(username = \
                logged_colab_user.username)[0]
            print(logged_taiga_user)
            projects = logged_taiga_user.projects.all().order_by('default_priority')
        
        kwargs['context']['projects'] = projects

        return super(DashboardMostRelevantProjectsWidget,
                     self).generate_content(**kwargs)
