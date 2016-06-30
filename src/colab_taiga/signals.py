import logging
import requests

from django.conf import settings
from django.dispatch import receiver

from colab.accounts.signals import user_created

from colab_taiga.models import TaigaUser


LOGGER = logging.getLogger('colab.plugins.taiga')

@receiver(user_created)
def create_taiga_user(sender, **kwargs):
    user = kwargs.get('user')
    password = kwargs.get('password')


    app_config = settings.COLAB_APPS.get('colab_taiga', {})
    upstream = app_config.get('upstream', '').rstrip('/')

    endpoint = '{}/api/v1/auth/register'.format(upstream)
    params = {
        'username': user.username,
        'password': password,
        'email': user.email,
        'full_name': user.get_full_name(),
        'type': 'public'
    }

    try:
        response = requests.post(endpoint, data=params)
    except Exception as exception:
        LOGGER.error("Error while connecting to Taiga API: %s" % exception)
        return
    
    if response.status_code == 201:
        taiga_user = TaigaUser(full_name=user.get_full_name(), is_active=True,
                               username=user.username)
        taiga_user.save()
        LOGGER.info("Taiga user %s created" % user.username)
    else:
        LOGGER.error("Unable to create %s Taiga user. HTTP Status: %s" %\
                     (user.username, response.status_code))
