from django.db import models

class StoredHttpRequest(models.Model):
    PRIORITIES = ((i, i) for i in range(1, 11))
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1, choices=PRIORITIES)

    def __unicode__(self):
        return "%s %s at %s (priority: %d)" % (self.method, self.path, str(self.created_at), self.priority)
