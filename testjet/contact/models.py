from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    bio = models.TextField()

class Contacts(models.Model):
    person = models.OneToOneField(Person, related_name='contacts')
    email = models.EmailField()
    jabber = models.EmailField()
    other = models.TextField()
