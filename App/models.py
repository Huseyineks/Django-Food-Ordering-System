from django.db import models
 
class App(models.Model):
 SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
 size = models.CharField(max_length=1,choices=SHIRT_SIZES)
