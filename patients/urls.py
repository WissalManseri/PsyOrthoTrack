from django.urls import path
from . import views

urlpatterns = [
    # Patient URLs
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/update/<int:pk>/', views.update_patient, name='update_patient'),
    path('patients/delete/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('patients/list/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:pk>/export_pdf/', views.export_patient_pdf, name='export_patient_pdf'),

    # Medical Record URLs
    path('medical_records/add/', views.add_medical_record, name='add_medical_record'),
    path('medical_records/update/<int:pk>/', views.update_medical_record, name='update_medical_record'),
    path('medical_records/delete/<int:pk>/', views.delete_medical_record, name='delete_medical_record'),
    path('medical_records/list/', views.medical_record_list, name='medical_record_list'),
    path('medical_records/<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
    path('medical_records/<int:pk>/export_pdf/', views.export_medical_record_pdf, name='export_medical_record_pdf'),
]
