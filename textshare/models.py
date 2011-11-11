from django.db import models

class Note(models.Model):
    text = models.CharField(max_length=12000)
    create_date = models.DateTimeField()
    key = models.IntegerField()
    pass_key = models.CharField(max_length=10,default='0000000000')
    
    def __unicode__(self):
        return str(self.key)