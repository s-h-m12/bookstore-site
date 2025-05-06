from django.db import models
from django.template.defaultfilters import title


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    cover = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.title