
from django.db import models

class Doctor(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('offline', 'Offline'),
    )

    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    image = models.ImageField(upload_to='doctors/')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    reviews = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    