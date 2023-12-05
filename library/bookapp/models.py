from django.db import models

class bookmanagement(models.Model):
    title=models.CharField(max_length=250)
    auther=models.CharField(max_length=250)
    genre=models.TextField()
    ISBN=models.BigAutoField()

def __str__(self):
    return f'{self.title}'



class patronmanagement(models.Model):
    name=models.CharField(max_length=50)
    contact_info=models.IntegerField()
    member_info=models.CharField()

def __str__(self)   :
    return f'{self.name}'




# Create your models here.
