from django.db import models

# Create your models here.
class Signin(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.fname + " " +self.lname
