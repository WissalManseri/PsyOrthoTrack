from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('update/<int:pk>/', views.update_patient, name='update_patient'),
    path('delete/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('patient/<int:pk>/export/', views.export_patient_pdf, name='export_patient_pdf'),
    
    path('add_medical_record/', views.add_medical_record, name='add_medical_record'),
    path('update_medical_record/<int:pk>/', views.update_medical_record, name='update_medical_record'),
    path('delete_medical_record/<int:pk>/', views.delete_medical_record, name='delete_medical_record'),
    path('medical_record/<int:pk>/export/', views.export_medical_record_pdf, name='export_medical_record_pdf'),

]
