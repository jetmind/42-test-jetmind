from django.core.management.base import BaseCommand
from django.db import models
import sys

class Command(BaseCommand):
    help = 'Prints all project models and the count of objects in every model'

    def handle(self, *args, **options):
        m_list = models.get_models()
        for m in m_list:
            line = '%s %s' % (m.__name__, m.objects.count())
            print line
            print >> sys.stderr, 'error: %s' % line
