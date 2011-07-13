from django.test import TestCase, Client
from contact.models import Person
from django.core.urlresolvers import reverse

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
        response = client.get(reverse('index'))
        self.assertContains(response, 'Igor', count=1, status_code=200)
        self.assertContains(response, 'Bondarenko', count=1)

class ChangeDataTest(TestCase):
    
    def test_change(self):
        c = Client()
        self.assertTrue(c.login(username='admin', password='admin'))
        c.post(reverse('edit'), {'name': 'jet', 'surname': 'mind', 'birth': '1988-03-29', 'bio': 'some bio', 
                          'email': 'jetmind2@gmail.com', 'jabber': 'i.bond@jabber.com.ua', 
                          'other': 'some info'})

        person = Person.objects.get(pk=1)
        self.assertEqual(person.name, 'jet')
        self.assertEqual(person.surname, 'mind')
        self.assertEqual(person.contacts.other, 'some info')

class WidgetTest(TestCase):
    
    def test_contains_js(self):
        js = '<script type="text/javascript" src="/static/js/calendar.js"></script>'
        c = Client()
        c.login(username='admin', password='admin')
        response = c.get(reverse('edit'))
        self.assertContains(response, js, count=1)