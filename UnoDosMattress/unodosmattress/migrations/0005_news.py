# Generated by Django 2.1.1 on 2018-11-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unodosmattress', '0004_auto_20181119_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('idNews', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
