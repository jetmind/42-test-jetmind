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


class ChangeDataTest(TestCase):
    
    def test_change(self):
        c = Client()
        self.assertTrue(c.login(username='admin', password='admin'))
        c.post('/edit/', {'name': 'jet', 'surname': 'mind'})

        person = Person.objects.get(pk=1)
        self.assertEqual(person.name, 'jet')
        self.assertEqual(person.surname, 'mind')
