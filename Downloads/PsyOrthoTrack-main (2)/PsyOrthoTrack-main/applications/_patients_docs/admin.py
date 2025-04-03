from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from applications.patients_docs.models import ProfilPatient
from django.utils.html import format_html
admin_site = admin.AdminSite(name='admin_personnalise')

admin.site.site_header = "PsyOrthoTrack"
# admin.site.site_title = "Admin - Gestion des Patients"
# admin.site.index_title = "Tableau de bord"

@admin.register(ProfilPatient)
class ProfilPatientAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'genre',  'date_de_rdv')
    list_filter = ('genre', 'cree_le', 'date_de_rdv')
    search_fields = ('prenom', 'nom', 'numero_telephone_1', 'numero_telephone_2')
    ordering = ('nom', 'prenom')
    verbose_name = "Documents et ressources "
    verbose_name_plural = "Documents et ressources "


    fieldsets = [
        ("Patients", {
            "fields": ['prenom', 'nom', 'genre', 'date_de_rdv'],
            "classes": ["tab"]
        }),
        ("Dossiers médicaux", {
            "fields": ["maladies_ou_handicaps_famille"],
            "classes": ["tab"]
        }),
    ]

    def view_medical_records_button(self, obj):
        return format_html(
            '<a class="button" href="/admin/patients_docs/medicalrecord/?patientidexact={}">📁 Voir Dossiers</a>',
            obj.id
        )
    view_medical_records_button.short_description = ""
