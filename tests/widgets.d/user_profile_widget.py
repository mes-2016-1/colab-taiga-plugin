from colab.widgets.widget_manager import WidgetManager
from colab_taiga.widgets.user_story import UserStoriesWidget


WidgetManager.register_widget('list', UserStoriesWidget())
