from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

class LogModel(models.Model):
    ACTION_CHOICES = (
            ('c', 'created'),
            ('e', 'edited'),
            ('d', 'deleted'),
    )
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
    model_class = models.CharField(max_length=255)

    def __unicode__(self):
        return "Model %s with id %d %s at %s" % (self.model_class, 
                self.model_id, self.get_action_display(), str(self.time))


def post_delete_callback(sender, **kwargs):
    if sender == LogModel:
        return

    log = LogModel(action='d')
    log.model_class = sender
    log.save()

def post_save_callback(sender, **kwargs):
    if sender == LogModel:
        return

    log = LogModel()
    if kwargs['created']:
        log.action = 'c'
    else:
        log.action = 'e'
    log.model_class = sender
    log.save()


post_delete.connect(post_delete_callback)
post_save.connect(post_save_callback)
