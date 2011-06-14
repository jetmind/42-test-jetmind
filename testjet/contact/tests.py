from django.test import TestCase
from contact.models import Contacts

class ContactsTest(TestCase):

    def setUp(self):
        self.contact = Contacts.objects.get(pk=1)

    def test_name(self):
        self.assertEqual(self.contact.name, 'Igor')
        self.assertEqual(self.contact.surname, 'Bondarenko')

    def test_contacts(self):
        self.assertEqual(self.contact.email, "jetmind2@gmail.com")
        self.assertEqual(self.contact.jabber, "i.bond@gmail.com")

    def test_bio(self):
        self.assertTrue(self.contact.bio != '')
