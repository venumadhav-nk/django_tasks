from django.db import models

# Create your models here.
class studentDetails(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    dob=models.DateField()

