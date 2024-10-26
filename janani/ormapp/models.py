from django.db import models
from django.contrib import admin
class Customer(models.Model):
    Name=models.CharField(max_length=10)
    accno=models.IntegerField(primary_key="accno")
    phno=models.IntegerField()
    income=models.IntegerField()
    Email=models.EmailField()
class CustomerAdmin(admin.ModelAdmin):
    list_display=('Name','accno','phno','income','Email')


