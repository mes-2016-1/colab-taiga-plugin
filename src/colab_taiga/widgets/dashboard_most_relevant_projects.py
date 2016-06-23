from colab.widgets.widget_manager import Widget
from colab_taiga.models import TaigaProject


class DashboardMostRelevantProjectsWidget(Widget):
    name = 'most relevant projects'
    template = 'widgets/dashboard_most_relevant_projects.html'

    def generate_content(self, **kwargs):
        projects = TaigaProject.all()
        kwargs['context']['projects'] = projects

        return super(DashboardMostRelevantProjectsWidget,
                     self).generate_content(**kwargs)
