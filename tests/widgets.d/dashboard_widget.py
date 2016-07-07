from colab.widgets.widget_manager import WidgetManager
from colab_taiga.widgets.dashboard_most_relevant_projects import DashboardMostRelevantProjectsWidget
from colab_taiga.widgets.user_stories import UserStoriesWidget


WidgetManager.register_widget(
    'dashboard', DashboardMostRelevantProjectsWidget())

WidgetManager.register_widget(
    'profile', UserStoriesWidget())
    