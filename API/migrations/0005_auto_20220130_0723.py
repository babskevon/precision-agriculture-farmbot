# Generated by Django 3.2.5 on 2022-01-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_alter_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensors',
            name='flowrate',
        ),
        migrations.AddField(
            model_name='sensors',
            name='flowrate1',
            field=models.CharField(blank=True, default=31.3, max_length=10),
        ),
        migrations.AddField(
            model_name='sensors',
            name='flowrate2',
            field=models.CharField(blank=True, default=31.3, max_length=10),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ImageField(null=True, upload_to='API/static/garden_pic'),
        ),
    ]