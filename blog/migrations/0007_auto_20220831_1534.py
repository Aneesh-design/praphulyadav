# Generated by Django 2.2.1 on 2022-08-31 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_notificatins'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notificatins',
            new_name='Notification',
        ),
    ]
