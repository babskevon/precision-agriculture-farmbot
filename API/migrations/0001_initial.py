# Generated by Django 3.2.5 on 2022-01-27 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light', models.CharField(blank=True, max_length=10)),
                ('humidity', models.CharField(blank=True, max_length=10)),
                ('temperature', models.CharField(blank=True, max_length=10)),
                ('flowrate1', models.CharField(blank=True, max_length=10)),
                ('flowrate2', models.CharField(blank=True, max_length=10)),
                ('soil_moisture', models.CharField(blank=True, max_length=10)),
                ('distance', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
