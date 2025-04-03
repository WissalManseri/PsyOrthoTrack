from django.db import models
from datetime import date
from django.utils import timezone

class PatientProfile(models.Model):
    gender_choices = [
                        ("M", "Male"),
                        ("F", "Female")
                    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField(editable=False)  # L'âge ne doit pas être modifiable directement
    gender = models.CharField(max_length=10, choices= gender_choices)
    address = models.CharField(max_length=200)
    phone_number_1 = models.CharField(max_length=10, unique=True )# Un numéro ne peut pas être utilisé deux fois
    phone_number_2 = models.CharField(max_length=10, unique=True , blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    picture = models.ImageField(upload_to="patient_pictures/", blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        unique_together = ('last_name', 'first_name')  # Empêche les doublons exacts
        ordering = ['last_name', 'first_name']
        verbose_name = "Profil patient"
        verbose_name_plural = "Profils patients"

    def save(self, *args, **kwargs):
        # Calculer l'âge basé sur la date de naissance
        today = date.today()
        self.age = today.year - self.date_of_birth.year 
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    record_date = models.DateField()
    description = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name} on {self.record_date}"

    class Meta:
        verbose_name = "Dossier médical"
        verbose_name_plural = "Dossiers médicaux"

