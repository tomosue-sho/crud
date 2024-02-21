from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
 
    def __str__(self):
        return self.name
    

    
    