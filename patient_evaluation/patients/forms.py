from django import forms
from .models import Patient, RendezVous

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
class RendezVousForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label="Sélectionnez un patient")

    class Meta:
        model = RendezVous
        fields = ['patient', 'date', 'heure']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'heure': forms.TimeInput(attrs={'type': 'time'}),
        }