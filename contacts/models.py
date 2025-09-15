from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="contacts",null=True ,blank=True)   # user.contact_set  => user.contacts
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  email = models.EmailField()
  phone = models.CharField(max_length=20)

  def __str__(self):
    return f"{self.name} {self.id}"

