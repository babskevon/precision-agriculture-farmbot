# Generated by Django 3.2.5 on 2022-11-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_auto_20220201_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='predict',
            field=models.CharField(default='healthy', max_length=150),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ImageField(null=True, upload_to='garden_pic'),
        ),
    ]
