from django.db import models

# Create your models here.
# table for storing the data fromc contact page

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name =models.CharField(max_length =50)
    phone =models.CharField(max_length=15)
    content=models.TextField()
    email =models.CharField(max_length=13)