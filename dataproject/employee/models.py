from django.db import models
from django.contrib import admin
# Create your models here.

class Employee(models.Model):
        
    employeeid=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    post=models.CharField(max_length=100)
    salary=models.FloatField()
    

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('employeeid','name','age','post','salary')