from django import forms
from .models import PatientProfile, MedicalRecord

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = '__all__'

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
