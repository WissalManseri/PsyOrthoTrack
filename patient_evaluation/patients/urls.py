from django.urls import path
from .views import ajouter_patient,detail_patient,generate_pdf,liste_patients,liste_rendez_vous,prendre_rendez_vous, ajouter_patient_modal

urlpatterns = [
    path('ajouter/', ajouter_patient, name='ajouter_patient'),
     path('liste_patients/', liste_patients, name='liste_patients'),
    path('<int:patient_id>/', detail_patient, name='detail_patient'),
    path('<int:patient_id>/pdf/', generate_pdf, name='generate_pdf'),
     path('rendez-vous/', liste_rendez_vous, name='liste_rendez_vous'),  # Voir les RDV
    path('rendez-vous/prendre/', prendre_rendez_vous, name='prendre_rendez_vous'),  # Prendre RDV
  path("ajouter/modal/", ajouter_patient_modal, name="ajouter_patient_modal"),  # ✅ Nouvelle route


]
