from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator

class User(AbstractUser):
    pass
class Speciality(models.Model):
    name=models.CharField(max_length=255)
class Doctor(User):
    license_number=models.CharField(max_length=6,unique=True,validators=[MaxLengthValidator(6) ,RegexValidator(r'^\d{6}$', message='License number must be exactly 6 digits.')])
    phone=models.CharField(max_length=8,validators=[MaxLengthValidator(8),RegexValidator(r'^\d{8}$', message='Phone number must be exactly 8 digits.')])
    speciality=models.ManyToManyField(Speciality,related_name='doctors')
class Patient(User):
    national_id=models.CharField(max_length=8,unique=True,validators=[MaxLengthValidator(8),RegexValidator(r'^\d{8}$', message='National ID must be exactly 8 digits.')])
    phone=models.CharField(max_length=8)
    birth_date=models.DateField()
