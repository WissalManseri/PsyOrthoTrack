# Generated by Django 5.1.7 on 2025-03-31 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("patients_docs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="medicalrecord",
            options={
                "verbose_name": "Dossier médical",
                "verbose_name_plural": "Dossiers médicaux",
            },
        ),
        migrations.AlterModelOptions(
            name="patientprofile",
            options={
                "ordering": ["last_name", "first_name"],
                "verbose_name": "Profil patient",
                "verbose_name_plural": "Profils patients",
            },
        ),
    ]
