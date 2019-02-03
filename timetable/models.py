from django.db import models

class Lessons(models.Model):
    title = models.CharField(max_length=30)
    less = models.TextField()

    def __str__(self):
        return self.title

