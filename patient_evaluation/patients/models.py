from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    diagnostic = models.TextField()
    date_de_naissance = models.DateField()
    date_de_traitement = models.DateField()
    
    # date_de_sortie = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=25,
        validators=[
            RegexValidator(regex=r'^\d{10}$', message="Le numéro de téléphone doit contenir exactement 10 chiffres.")
        ],
        unique=True  # Un numéro ne peut pas être utilisé deux fois
    )
    email = models.EmailField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'prenom')  # Empêche les doublons exacts
        
    def __str__(self):
        return f"{self.name} {self.prenom}"
    
class RendezVous(models.Model):
        patient = models.ForeignKey('Patient', on_delete=models.CASCADE)  # Un patient peut avoir plusieurs RDV
        date = models.DateField()
        heure = models.TimeField()
        description = models.TextField()
        class Meta:
            unique_together = ('date', 'heure')  # Empêche deux RDV au même moment

        def __str__(self):
            return f"RDV: {self.patient.name} {self.patient.prenom} - {self.date} à {self.heure}"