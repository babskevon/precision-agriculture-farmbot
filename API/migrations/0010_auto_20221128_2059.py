# Generated by Django 3.2.5 on 2022-11-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_auto_20221128_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='bean_score',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='stress_score',
            field=models.CharField(max_length=150, null=True),
        ),
    ]