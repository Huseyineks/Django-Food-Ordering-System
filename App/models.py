from django.db import models
 
class Options(models.Model):
 
 size = models.CharField(max_length=10)
 temp = models.CharField(max_length=20)
 request = models.TextField()

