from colab.widgets.widget_manager import Widget
from colab_taiga.models import TaigaProject, TaigaUser


class UserStoriesWidget(Widget):
    name = 'user stories'
    template = 'widgets/user_stories.html'

    def generate_content(self, **kwargs):
        user_stories = []

        if kwargs['context']['user'].is_authenticated():
            logged_colab_user = kwargs['context']['user']
            logged_taiga_user = TaigaUser.objects.get(username = \
                logged_colab_user.username)
            user_stories = logged_taiga_user.own_userstory.filter(is_closed = False).order_by('total_points')
        
        kwargs['context']['user_stories'] = user_stories

        return super(UserStoriesWidget,
                     self).generate_content(**kwargs)
