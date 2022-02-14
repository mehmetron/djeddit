
from django.db import models
import datetime
from django.utils import timezone

class Thread(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    subs = models.ForeignKey('Sub', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)


class Sub(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField('date published')

    def __str__(self):
        return self.name

