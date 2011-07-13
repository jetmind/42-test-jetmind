from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class TagTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_edit_link_tag(self):
        response = self.client.get(reverse('index'))
        #self.assertContains(response, '/admin/contact/person/1/', count=1, status_code=200)
        self.assertContains(response, reverse('admin:contact_person_change', args=(1,)), count=1, status_code=200)
