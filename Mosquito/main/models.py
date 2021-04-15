from django.db import models

# Create your models here.
class local(models.Model):
    name = models.CharField(max_length=10, null=False)
    year = models.CharField(max_length=10, null=False)
    month = models.CharField(max_length=10, null=False)
    day = models.CharField(max_length=10, null=False)
    
    def __str__(self):
        return self.name
    
class detection(models.Model):
    name = models.CharField(max_length=20, null=False)
    lat = models.CharField(max_length=20, null=False)
    lot = models.CharField(max_length=20, null=False)