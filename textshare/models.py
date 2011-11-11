from django.db import models

class Note(models.Model):
    text = models.CharField(max_length=12000)
    create_date = models.DateTimeField()
    key = models.IntegerField()
    
    def __unicode__(self):
        return str(self.key)