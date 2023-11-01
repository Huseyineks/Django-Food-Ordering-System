from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=20)
  image = models.ImageField(upload_to='img')
  price = models.BigIntegerField()
  content = models.TextField()
  def __str__(self):
   return self.name

class Options(models.Model):
 
 size = models.CharField(max_length=10)
 temp = models.CharField(max_length=20)
 request = models.TextField(blank=True,null=True)
 

 def __str__(self):
   return 'Details'

class Paying(models.Model):

   payoptions = models.CharField(max_length=50)

   def __str__(self):
     return self.payoptions

