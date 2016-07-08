from colab.plugins.views import ColabProxyView


class TaigaPluginProxyView(ColabProxyView):
    app_label = 'colab_taiga'
    diazo_theme_template = 'proxy/taiga.html'
    add_remote_user = True
