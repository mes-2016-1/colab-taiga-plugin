from mock import Mock, patch

from django.test import TestCase, Client

#from coalb_taiga.models import TaigaUser
from colab_taiga.signals import create_taiga_user


class ColabTaigaTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.mocked_settings = {
            'colab_taiga': { 'upstream': "https://taiga.url/api" }
        }
        self.mocked_user = Mock(
            email="test@email.com",
            username="test",
            get_full_name=lambda: "Test User"
        )
        super(ColabTaigaTest, self).setUp()

    @patch('colab_taiga.signals.LOGGER.info')
    @patch('colab_taiga.signals.settings.COLAB_APPS')
    @patch('colab_taiga.signals.requests.post')
    def test_taiga_user_creation(self, requests_post_mock, settings_mock,
                                 logger_info_mock):
        requests_post_mock.return_value = Mock(status_code=201)
        settings_mock.return_value = self.mocked_settings

        create_taiga_user(None, user=self.mocked_user, password="secret")
        logger_info_mock.assert_called_once() 

    @patch('colab_taiga.signals.LOGGER.error')
    @patch('colab_taiga.signals.settings.COLAB_APPS')
    @patch('colab_taiga.signals.requests.post')
    def test_taiga_user_creation_api_error(self, requests_post_mock,
                                           settings_mock, logger_error_mock):
        requests_post_mock.return_value = Mock(status_code=500)
        settings_mock.return_value = self.mocked_settings 

        create_taiga_user(None, user=self.mocked_user, password="secret")
        logger_error_mock.assert_called_once() 

    @patch('colab_taiga.signals.LOGGER.error')
    @patch('colab_taiga.signals.settings.COLAB_APPS')
    @patch('colab_taiga.signals.requests.post')
    def test_taiga_user_creation_connection_error(self, requests_post_mock,
                                         settings_mock, logger_error_mock):
        requests_post_mock.side_effect = Exception
        settings_mock.return_value = self.mocked_settings 

        create_taiga_user(None, user=self.mocked_user, password="secret")
        logger_error_mock.assert_called_once() 
