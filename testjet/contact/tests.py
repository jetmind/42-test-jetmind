from django.test import TestCase, Client
from contact.models import Person

class ContactsTest(TestCase):

    def setUp(self):
        self.person = Person.objects.get(pk=1)

    def test_name(self):
        self.assertEqual(self.person.name, 'Igor')
        self.assertEqual(self.person.surname, 'Bondarenko')

    def test_contacts(self):
        self.assertEqual(self.person.contacts.email, "jetmind2@gmail.com")
        self.assertEqual(self.person.contacts.jabber, "i.bond@jabber.com.ua")

    def test_bio(self):
        self.assertTrue(self.person.bio != '')

    def test_page_content(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Igor', count=1, status_code=200)
        self.assertContains(response, 'Bondarenko', count=1)
