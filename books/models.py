from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=240)
    specifications = models.FileField(upload_to='')

    def __str__(self):
        return self.title
