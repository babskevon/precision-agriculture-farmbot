# Generated by Django 3.2.5 on 2023-07-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0015_fileupdate_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupdate',
            name='version',
            field=models.CharField(default='1.0.0', max_length=20),
        ),
    ]
