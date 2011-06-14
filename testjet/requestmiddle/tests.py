from django.test import TestCase, Client
from testjet.requestmiddle.models import StoredHttpRequest

class MiddlewareTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_middleware(self):
        self.client.get('/')
        req = StoredHttpRequest.objects.all().order_by('-created_at')[0]
        self.assertEqual(req.path, '/')
        self.assertEqual(req.method, 'GET')


class ContextProcessorTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_context_processor(self):
        response = self.client.get('/')
        self.assertTrue('settings' in response.context)
