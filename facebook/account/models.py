from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    dob=models.DateField()

    def __str__(self):
        return self.name
class employe(models.Model):
    name=models.CharField(max_length=50)
    salary=models.IntegerField(max_length=20)
    gender=models.CharField( max_length=50)
    role=models.CharField(max_length=20)
    shift=models.CharField( max_length=50)

    def __str__(self):
        return self.name