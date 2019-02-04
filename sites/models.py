from django.db import models

class Sites(models.Model):
    title = models.CharField(max_length=200)
    site = models.TextField()

    def __str__(self):
        return self.title
