from colab.plugins.views import ColabProxyView


class TaigaPluginProxyView(ColabProxyView):
    app_label = 'colab_taiga'
    diazo_theme_template = 'proxy/taiga.html'

    def get_proxy_request_headers(self, request):
        headers = super(TaigaPluginProxyView,
                        self).get_proxy_request_headers(request)

        if request.user.is_authenticated():
            headers["Auth-user"] = request.user.username

        return headers
