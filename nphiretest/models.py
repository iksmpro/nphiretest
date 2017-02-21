from django.db import models

class LogObject(models.Model):
    time = models.DateTimeField('Creation time')
    text = models.TextField() #max_length=1024)