# Generated by Django 2.0.5 on 2018-10-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageBed', '0020_auto_20181003_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientNumber', models.IntegerField(default=0)),
                ('doctorsID', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='contactNum',
            field=models.CharField(max_length=11),
        ),
    ]
