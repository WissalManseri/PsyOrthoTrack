from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import PatientProfile, MedicalRecord
from .forms import PatientProfileForm, MedicalRecordForm

import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string


def add_patient(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient ajouté avec succès.')
            return redirect('patient_list')  # Assurez-vous d'avoir une vue nommée 'patient_list'
        else:
            messages.error(request, 'Erreur lors de l\'ajout du patient.')
    else:
        form = PatientProfileForm()
    return render(request, 'patient_profile/add_patient.html', {'form': form})

def update_patient(request, pk):
    patient = get_object_or_404(PatientProfile, pk=pk)
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient mis à jour avec succès.')
            return redirect('patient_detail', pk=pk)  # Assurez-vous d'avoir une vue nommée 'patient_detail'
        else:
            messages.error(request, 'Erreur lors de la mise à jour du patient.')
    else:
        form = PatientProfileForm(instance=patient)
    return render(request, 'patient_profile/update_patient.html', {'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(PatientProfile, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient supprimé avec succès.')
        return redirect('patient_list')  # Assurez-vous d'avoir une vue nommée 'patient_list'
    return render(request, 'patient_profile/delete_patient.html', {'patient': patient})

def export_patient_pdf(request, pk):
    patient = PatientProfile.objects.get(pk=pk)
    
    # Convertir le template HTML en une chaîne
    html = render_to_string('patient_profile/pdf_template.html', {'patient': patient})

    # Configuration de pdfkit avec le bon chemin vers wkhtmltopdf
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    # Génération du PDF à partir de la chaîne HTML
    pdf = pdfkit.from_string(html, False, configuration=pdfkit_config)

    # Retourner le PDF en réponse HTTP
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="patient_{pk}.pdf"'

    return response


def add_medical_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dossier médical ajouté avec succès.')
            return redirect('medical_record_list')  # Assurez-vous d'avoir une vue nommée 'medical_record_list'
        else:
            messages.error(request, 'Erreur lors de l\'ajout du dossier médical.')
    else:
        form = MedicalRecordForm()
    return render(request, 'medical_record/add_medical_record.html', {'form': form})

def update_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dossier médical mis à jour avec succès.')
            return redirect('medical_record_detail', pk=pk)  # Assurez-vous d'avoir une vue nommée 'medical_record_detail'
        else:
            messages.error(request, 'Erreur lors de la mise à jour du dossier médical.')
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'medical_record/update_medical_record.html', {'form': form})

def delete_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        medical_record.delete()
        messages.success(request, 'Dossier médical supprimé avec succès.')
        return redirect('medical_record_list')  # Assurez-vous d'avoir une vue nommée 'medical_record_list'
    return render(request, 'medical_record/delete_medical_record.html', {'medical_record': medical_record})

def export_medical_record_pdf(request, pk):
    record = MedicalRecord.objects.get(pk=pk)
    
    # Convertir le template HTML en une chaîne
    html = render_to_string('medical_record/pdf_template.html', {'record': record})

    # Configuration de pdfkit avec le bon chemin vers wkhtmltopdf
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    # Génération du PDF à partir de la chaîne HTML
    pdf = pdfkit.from_string(html, False, configuration=pdfkit_config)

    # Retourner le PDF en réponse HTTP
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="medical_record_{pk}.pdf"'

    return response