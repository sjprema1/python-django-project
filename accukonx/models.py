from django.db import models

class Person(models.Model):
    name = models.CharField(max_length =100)
    age = models.IntegerField(max_length =50)
    dob = models.DateField()






