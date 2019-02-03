from django.db import models

class Parent(models.Model):
    title = models.CharField(max_length=200)
    less = models.TextField()

    def __str__(self):
        return self.title
