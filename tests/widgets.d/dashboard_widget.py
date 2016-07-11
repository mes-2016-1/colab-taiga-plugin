from colab.widgets.widget_manager import WidgetManager
from colab_taiga.widgets.dashboard_most_relevant_projects import DashboardMostRelevantProjectsWidget


WidgetManager.register_widget(
    'dashboard', DashboardMostRelevantProjectsWidget())


    