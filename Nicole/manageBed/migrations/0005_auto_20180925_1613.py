# Generated by Django 2.0.5 on 2018-09-25 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageBed', '0004_auto_20180925_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartrate',
            name='idPatient',
        ),
        migrations.RemoveField(
            model_name='patient_table',
            name='idPatient',
        ),
        migrations.RemoveField(
            model_name='position',
            name='idPatient',
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='idPatient',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]