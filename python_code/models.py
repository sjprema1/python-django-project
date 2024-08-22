from django.db import models
from datetime import date

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    qualification = models.CharField(max_length=10)

class meta :
    db_table = "employee_tbl"
