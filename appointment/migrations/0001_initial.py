# Generated by Django 5.1.4 on 2024-12-12 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('patient_name', models.CharField(max_length=250)),
                ('doctor', models.CharField(max_length=250)),
                ('time', models.TimeField()),
                ('file_number', models.CharField(max_length=20, unique=True)),
                ('is_doctor', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_number', models.CharField(max_length=250, unique=True)),
                ('doctor_name', models.CharField(max_length=250)),
                ('patient_name', models.CharField(max_length=250)),
                ('file_number', models.CharField(max_length=20, unique=True)),
                ('is_doctor', models.BooleanField(default=False)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment')),
            ],
        ),
    ]
