from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import PatientProfile, MedicalRecord
from .forms import PatientProfileForm, MedicalRecordForm
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit

pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

def add_patient(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient ajouté avec succès.')
            return redirect('patient_list')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du patient.')
    else:
        form = PatientProfileForm()
    return render(request, 'patient/add_patient.html', {'form': form})

def update_patient(request, pk):
    patient = get_object_or_404(PatientProfile, pk=pk)
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient mis à jour avec succès.')
            return redirect('patient_detail', pk=pk)
        else:
            messages.error(request, 'Erreur lors de la mise à jour du patient.')
    else:
        form = PatientProfileForm(instance=patient)
    return render(request, 'patient/update_patient.html', {'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(PatientProfile, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient supprimé avec succès.')
        return redirect('patient_list')
    return render(request, 'patient/delete_patient.html', {'patient': patient})

def add_medical_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dossier médical ajouté avec succès.')
            return redirect('medical_record_list')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du dossier médical.')
    else:
        form = MedicalRecordForm()
    return render(request, 'patient/add_medical_record.html', {'form': form})

def update_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dossier médical mis à jour avec succès.')
            return redirect('medical_record_detail', pk=pk)
        else:
            messages.error(request, 'Erreur lors de la mise à jour du dossier médical.')
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'patient/update_medical_record.html', {'form': form})

def delete_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        medical_record.delete()
        messages.success(request, 'Dossier médical supprimé avec succès.')
        return redirect('medical_record_list')
    return render(request, 'patient/delete_medical_record.html', {'medical_record': medical_record})

def export_patient_pdf(request, pk):
    patient = get_object_or_404(PatientProfile, pk=pk)
    template_path = 'patient_profile/pdf_template.html'
    context = {'patient': patient}
    html = render_to_string(template_path, context)
    pdf = pdfkit.from_string(html, False, configuration=pdfkit_config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="patient_{patient.pk}.pdf"'
    return response

def export_medical_record_pdf(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    template_path = 'medical_record/pdf_template.html'
    context = {'medical_record': medical_record}
    html = render_to_string(template_path, context)
    pdf = pdfkit.from_string(html, False, configuration=pdfkit_config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="medical_record_{medical_record.pk}.pdf"'
    return response
