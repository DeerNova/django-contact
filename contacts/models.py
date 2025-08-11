from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  email = models.EmailField()
  phone = models.CharField(max_length=20)

  def __str__(self):
    return f"{self.name} {self.id}"
   