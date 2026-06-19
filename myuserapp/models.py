from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField("Name",max_length=30)
    mobile = models.CharField("Number",max_length=10)
    email = models.EmailField("Email",blank=False)

    def __str__(self):
        return self.name
