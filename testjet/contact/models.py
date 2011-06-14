from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    bio = models.TextField()

class Contacts(models.Model):
    person = models.ForeignKey(Person, related_name='contacts')
    birth = models.DateField()
    email = models.EmailField()
    jabber = models.EmailField()
    other = models.TextField()
