from django.test import TestCase, Client
from django.conf import settings
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

class ContextProcessorTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_context_processor(self):
        response = self.client.get('/')
        try:
            s = response.context['settings']
        except:
            s = False
        self.assertTrue(s)
        self.assertEqual(s, settings)


class PriorityTest(TestCase):

    def test_priority(self):
        page = '/login/'
        self.client.get(page)
        self.client.get(page)
        response = self.client.get('/requests/')
        self.assertContains(response, '(priority: 1) GET %s' % page, count=2)
        prior = 100
        self.client.post('/requests/', {'priority': prior, 'requestid': 1})
        response = self.client.get('/requests/')
        self.assertContains(response, '(priority: %d) GET %s' % (prior, page), count=1)
