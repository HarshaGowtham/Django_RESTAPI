from pdb import post_mortem
from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_id =  models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    deleted = models.CharField(max_length=1)
    


#create / add / insert - POST 
#Retrieve / fetch - GET
#update / edit - PUT
#delete / remove - DELETE