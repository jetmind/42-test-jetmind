from django.db import models

# Create your models here.

class LogModel(models.Model):
    ACTION_CHOICES = (
            ('c', 'created'),
            ('e', 'edited'),
            ('d', 'deleted'),
    )
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
    model_class = models.CharField(max_length=255)
    model_id = models.IntegerField()

    def __unicode__(self):
        return "Model %s with id %d %s at %s" % (self.model_class, 
                self.model_id, self.get_action_display(), str(self.time))
