# Generated by Django 3.2.5 on 2023-07-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0017_alter_fileupdate_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupdate',
            name='file',
            field=models.FileField(upload_to='updates'),
        ),
    ]
