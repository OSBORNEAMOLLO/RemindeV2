# Generated by Django 5.1.4 on 2024-12-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]