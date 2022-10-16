from gzip import FNAME
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class People(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    person_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
