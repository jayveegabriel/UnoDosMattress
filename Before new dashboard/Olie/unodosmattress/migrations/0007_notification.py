# Generated by Django 2.1.1 on 2018-11-01 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unodosmattress', '0006_auto_20181027_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('idNotification', models.AutoField(primary_key=True, serialize=False)),
                ('idBeds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unodosmattress.Beds')),
            ],
        ),
    ]
