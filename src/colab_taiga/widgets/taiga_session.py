from colab.widgets.widget_manager import Widget

class TaigaSessionWidget(Widget):
    name = 'Taiga Session Widget'
    template = 'widgets/taiga_session_widget.html'

    def generate_content(self, **kwargs):
        return super(TaigaSessionWidget, self).generate_content(**kwargs)
