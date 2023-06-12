from django.db import models

# Create your models here.

class search(models.Model):
    find=models.CharField(max_length=100,blank=False,null=False)
