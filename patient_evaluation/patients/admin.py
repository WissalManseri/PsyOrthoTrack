from django.contrib import admin

from .models import Patient, RendezVous 

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'prenom', 'phone_number', 'email', 'date_de_naissance')
    search_fields = ('name', 'prenom', 'phone_number', 'email')
    list_filter = ('gender', 'date_de_traitement')
    ordering = ('name', 'prenom')

@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'heure')
    search_fields = ('patient__name', 'patient__prenom', 'date')
    list_filter = ('date',)
    ordering = ('date', 'heure')