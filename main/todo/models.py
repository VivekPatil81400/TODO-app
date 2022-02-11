from django.db import models

# Create your models here.

class Todoitems(models.Model):

    def __str__(self):
        return self.content

    content = models.TextField()