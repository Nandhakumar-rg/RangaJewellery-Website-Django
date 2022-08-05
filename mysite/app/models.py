from email.policy import default
from pyexpat import model
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
from django.db import models

# Create your models here.
class sign(models.Model):
    fname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='images/profiles', default='https://i.pinimg.com/originals/51/f6/fb/51f6fb256629fc755b8870c801092942.png')
    gender = models.CharField(max_length=100)
    dob = models.CharField(null=True,blank=True,max_length=30)
    address = models.CharField(max_length=200,default="Your address")


class adminsite(models.Model):
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    

class move(models.Model):
    url = models.CharField(max_length=500)

class jewel(models.Model):
    id=models.IntegerField(primary_key=True)
    jname = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    
class Itemcart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    icname = models.CharField(max_length=100)
    icurl = models.CharField(max_length=500)
    icprice = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    uname = models.CharField(max_length=100, default="null")

class orders(models.Model):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4, editable= False)
    ocname = models.CharField(max_length=100)
    ocurl = models.CharField(max_length=500)
    ocprice = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    uname = models.CharField(max_length=100, default="null")
    address = models.CharField(max_length=100, default="")

def __unicode__(self):        #if error use this function
    return self.name 