from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()  # Use DateField for dates
    patient_name = models.CharField(max_length=250)
    doctor = models.CharField(max_length=250)  # Ideally, this could be another User or Profile model
    time = models.TimeField()  # Use TimeField for times
    file_number = models.CharField(max_length=20, unique=True)  # Assuming file_number should be unique
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor} - {self.patient_name}"


class Consultation(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    consultation_number = models.CharField(max_length=250, unique=True)  # Unique if necessary
    doctor_name = models.CharField(max_length=250)
    patient_name = models.CharField(max_length=250)
    file_number = models.CharField(max_length=20, unique=True)  # Assuming file_number should be unique
    is_doctor = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor_name} - {self.patient_name}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username
