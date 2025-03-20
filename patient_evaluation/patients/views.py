from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import pdfkit
from .models import Patient
from django.contrib import messages
from .forms import PatientForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# Configuration pour Windows (mets le bon chemin)



def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, "patients/liste_patients.html", {"patients": patients})


def detail_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, "patients/detail_patient.html", {"patient": patient})

from django.template.loader import render_to_string



# Configuration pour Windows
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

def generate_pdf(request, patient_id):
    # Récupérer l'objet patient ou retourner une 404
    patient = get_object_or_404(Patient, id=patient_id)

    # Générer le contenu HTML depuis le template
    html = render_to_string("patients/pdf_template.html", {"patient": patient})

    # Générer le PDF avec pdfkit
    pdf = pdfkit.from_string(html, False, configuration=PDFKIT_CONFIG)

    # Télécharger le PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Patient_{patient.name}_{patient.prenom}.pdf"'
    return response

from .models import RendezVous
from .forms import RendezVousForm
import time
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient
from .forms import PatientForm

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Patient, RendezVous
from .forms import PatientForm, RendezVousForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatientForm

def ajouter_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le patient a été ajouté avec succès !")  # 🔥 Message de succès
            return redirect("ajouter_patient")  # 🔄 Redirection pour effacer les champs après soumission
    else:
        form = PatientForm()

    return render(request, "patients/formulaire.html", {"form": form})

def prendre_rendez_vous(request):
    if not Patient.objects.exists():
        messages.warning(request, "⚠ Aucun patient trouvé. Veuillez d'abord ajouter un patient.")
        return redirect('ajouter_patient')

    if request.method == "POST":
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Rendez-vous enregistré avec succès !")
            return redirect('liste_rendez_vous')
    else:
        form = RendezVousForm()

    return render(request, 'patients/prendre_rendez_vous.html', {'form': form})  # 🔹 Ajoute "patients/"
def liste_rendez_vous(request):
    rendez_vous = RendezVous.objects.all().order_by('date', 'heure')  # Trie par date et heure
    return render(request, 'patients/liste_rendez_vous.html', {'rendez_vous': rendez_vous})
from django.shortcuts import render
from .forms import PatientForm

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import PatientForm

def ajouter_patient_modal(request):
    form = PatientForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Patient ajouté avec succès !")

        # 🔥 Réponse HTMX pour afficher le message, fermer la modale et recharger la page
        return HttpResponse("""
            <script>
                alert('Patient ajouté avec succès !');
                htmx.trigger('#reload-page', 'refresh');  // 🔥 Recharge la page
                var modal = bootstrap.Modal.getInstance(document.getElementById('addPatientModal'));
                modal.hide();  // 🔥 Ferme la modale
            </script>
        """)

    return render(request, "patients/partials/ajouter_patient_modal.html", {"form": form})
