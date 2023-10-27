from django.db import models
 
class Options(models.Model):
 
 size = models.CharField(max_length=10)
 temp = models.CharField(max_length=20)
 request = models.TextField()
 created_at = models.DateTimeField(auto_now_add=True)

 def __str__(self):
   return 'Details'

class Paying(models.Model):

   payoptions = models.CharField(max_length=50) 

