from django.db import models

# Create your models here.

class Events(models.Model):
    id = models.UUIDField(primary_key=True)
    event_title = models.CharField(max_length=200)
    event_volunteer = models.IntegerField(default=0)
    event_date = models.DateTimeField()

