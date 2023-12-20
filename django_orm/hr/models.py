from django.db import models
from django.utils import timezone

# Create your models here.

# class Compensation(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.phone
    

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.CharField(max_length=10000)
    age = models.SmallIntegerField(null=True)
    created = models.DateTimeField(default=timezone.now)
    work_experience = models.SmallIntegerField(default=0, null=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'