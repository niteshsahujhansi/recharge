from django.db import models

# Create your models here.

class Combo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    net = models.CharField(max_length=40)
    talk = models.CharField(max_length=40)
    vald = models.CharField(max_length=40)
    price = models.IntegerField()   
    text = models.TextField()
    def __str__(self):
        return f" A  {self.name} plan with  {self.talk}rs talkitime,{self.net} data package and validity of {self.vald} days"

class Internet(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    net = models.CharField(max_length=40)
    vald = models.CharField(max_length=40)
    price = models.IntegerField()   
    text = models.TextField()
    def __str__(self):
        return f" A  {self.name} plan with  {self.net} data package and validity of {self.vald} days"


class Talktime(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    talk = models.CharField(max_length=40)
    vald = models.CharField(max_length=40)
    price = models.IntegerField()   
    text = models.TextField()   
    def __str__(self):
        return f" A  {self.name} plan with  {self.talk}rs talkitime and validity of {self.vald} days"