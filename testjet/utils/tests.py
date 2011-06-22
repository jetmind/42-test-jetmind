from django.test import TestCase, Client

class TagTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_edit_link_tag(self):
        response = self.client.get('/')
        self.assertContains(response, '/admin/contact/person/1/', count=1, status_code=200)
