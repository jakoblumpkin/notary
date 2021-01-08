from django.db import models

# Create your models here.

class Review(models.Model):
    email=models.EmailField()
    message=models.CharField(max_length=250)
    date=models.DateTimeField(null=True, blank=True)
