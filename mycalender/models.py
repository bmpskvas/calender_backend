from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    description = models.CharField(max_length=500)
    start_time = models.DateTimeField() 
    end_time = models.DateTimeField()
    
  