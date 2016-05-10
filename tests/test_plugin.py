
from django.test import TestCase, Client


class ColabTaigaPluginPluginTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_true(self):
        assert True
