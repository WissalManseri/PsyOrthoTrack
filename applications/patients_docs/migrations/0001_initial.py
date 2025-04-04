# Generated by Django 5.1.7 on 2025-03-31 18:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PatientProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("age", models.IntegerField(editable=False)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=10
                    ),
                ),
                ("address", models.CharField(max_length=200)),
                ("phone_number_1", models.CharField(max_length=10, unique=True)),
                (
                    "phone_number_2",
                    models.CharField(blank=True, max_length=10, null=True, unique=True),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="patient_pictures/"
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "unique_together": {("last_name", "first_name")},
            },
        ),
        migrations.CreateModel(
            name="MedicalRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("record_date", models.DateField()),
                ("description", models.TextField()),
                ("prescription", models.TextField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients_docs.patientprofile",
                    ),
                ),
            ],
        ),
    ]
