from django.test import TestCase
from testjet.contact.models import Person
from testjet.logmodel.models import LogModel
import datetime

class SignalsTest(TestCase):
    
    def test_creation(self):
        person = Person()
        person.name = 'Test'
        person.surname = 'Test'
        person.birth = datetime.datetime.now()
        person.bio = 'Some bio'
        person.save()
        
        log = LogModel.objects.all().order_by('-time')[0]
        self.assertEquals(log.action, 'c')
        self.assertEquals(unicode(log.model_class), unicode(person.__class__))

    def test_edition(self):
        person = Person.objects.get(id=1)
        person.name = 'NewName'
        person.save()

        log = LogModel.objects.all().order_by('-time')[0]
        self.assertEquals(log.action, 'e')
        self.assertEquals(unicode(log.model_class), unicode(person.__class__))


    def test_deletion(self):
        person = Person.objects.get(id=1)
        person.delete()

        log = LogModel.objects.all().order_by('-time')[0]
        self.assertEquals(log.action, 'd')
        self.assertEquals(unicode(log.model_class), unicode(person.__class__))
