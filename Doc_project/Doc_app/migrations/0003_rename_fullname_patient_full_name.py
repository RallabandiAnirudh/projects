# Generated by Django 4.1.4 on 2022-12-22 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Doc_app", "0002_patient_delete_clinic"),
    ]

    operations = [
        migrations.RenameField(
            model_name="patient", old_name="fullname", new_name="full_name",
        ),
    ]
