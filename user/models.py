from django.db import models

class OrderedItem(models.Model):
  user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
  name = models.CharField(max_length=20)
  price = models.BigIntegerField()
  size = models.CharField(max_length=10)
  temp = models.CharField(max_length=20)
  request = models.TextField()
  payoptions = models.CharField(max_length=50)
  image = models.ImageField(upload_to='img')
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.name
  
