from django.db import models
from datetime import date

class PatientProfile(models.Model):
    gender_choices = [
                        ("M", "Male"),
                        ("F", "Female")
                    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices= gender_choices)
    address = models.TextField()
    phone_number_1 = models.CharField(max_length=10)
    phone_number_2 = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    picture = models.ImageField(upload_to="patient_pictures/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    record_date = models.DateField()
    description = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name} on {self.record_date}"
