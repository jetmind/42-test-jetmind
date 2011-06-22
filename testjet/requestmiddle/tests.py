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

    def test_ten(self):
        
        urls = ('/', '/a/', '/b/', '/c/', '/d/')

        # Check if last ten request displayed on page
        for i, url in enumerate(urls, start=1):
            self.client.get(url)
            response = self.client.get('/requests/')
            self.assertContains(response, 'GET %s ' % url, count=1)
            self.assertContains(response, 'GET /requests/ ', count=i)

        
        # Make 11-ths request and check if first request not displayed now
        response = self.client.get('/requests/')
        self.assertNotContains(response, 'GET %s ' % urls[0])
