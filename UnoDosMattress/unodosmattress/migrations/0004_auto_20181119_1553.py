# Generated by Django 2.1.1 on 2018-11-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unodosmattress', '0003_auto_20181117_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='rfid',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='rfid',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
