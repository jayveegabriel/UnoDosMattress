# Generated by Django 2.0.5 on 2018-09-28 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageBed', '0015_auto_20180927_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartrate',
            name='idRefHeart',
        ),
        migrations.AlterField(
            model_name='heartrate',
            name='idPatient',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Ref_HeartRate',
        ),
    ]
