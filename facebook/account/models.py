from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    dob=models.DateField()

    def __str__(self):
        return self.name
