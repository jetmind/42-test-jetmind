from django.test import TestCase
from contact.models import Person

class ContactsTest(TestCase):

    def setUp(self):
        self.person = Person.objects.get(pk=1)

    def test_name(self):
        self.assertEqual(self.person.name, 'Igor')
        self.assertEqual(self.person.surname, 'Bondarenko')

    def test_contacts(self):
        self.assertEqual(self.person.contacts.email, "jetmind2@gmail.com")
        self.assertEqual(self.person.contacts.jabber, "i.bond@gmail.com")

    def test_bio(self):
        self.assertTrue(self.person.bio != '')
