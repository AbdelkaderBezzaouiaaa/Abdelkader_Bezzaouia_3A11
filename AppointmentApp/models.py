from django.db import models
from AccountApp.models import Doctor, Patient
from django.db.models.fields import Field

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'
    reason = models.CharField(max_length=255)
    prescription = models.FileField(upload_to='prescriptions/')
    duration_minutes = models.PositiveIntegerField()
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=9, choices=Status.choices,
        default=Status.PENDING)
      
    doctor = models.ForeignKey(
        'AccountApp.Doctor', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(
        'AccountApp.Patient', on_delete=models.CASCADE, related_name='appointments')