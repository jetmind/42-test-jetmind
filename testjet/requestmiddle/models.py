from django.db import models

# Create your models here.
class StoredHttpRequest(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s at %s" % (self.method, self.path, str(self.created_at))
