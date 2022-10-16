from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
