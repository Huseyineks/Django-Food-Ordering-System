from django.db import models

class OrderedItem(models.Model):
  name = models.CharField(max_length=20)
  price = models.BigIntegerField()
  size = models.CharField(max_length=10)
  temp = models.CharField(max_length=20)
  request = models.TextField()
  payoptions = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.name
  
