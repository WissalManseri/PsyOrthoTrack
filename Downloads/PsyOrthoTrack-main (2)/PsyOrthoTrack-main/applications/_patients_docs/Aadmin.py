from django.contrib  import admin
from django.contrib.admin.sites import AdminSite
from applications.patients_docs.Mmodels import PatientProfile, MedicalRecord

admin_site = admin.AdminSite(name='custom_admin')

admin.site.site_header = "PsyOrthoTrack"
# admin.site.site_title = "Admin - Gestion des Patients"
# admin.site.index_title = "Tableau de Bord"


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender')
    list_filter = ('gender', 'created_at') #, 'created_at'
    search_fields = ('first_name', 'last_name', 'phone_number_1')
    ordering = ('last_name', 'first_name')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'record_date', 'description')
    list_filter = ('record_date',)
    search_fields = ('patient__first_name', 'patient__last_name', 'description')
    ordering = ('record_date',)
