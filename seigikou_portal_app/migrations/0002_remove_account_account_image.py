# Generated by Django 3.1.2 on 2022-02-05 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seigikou_portal_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='account_image',
        ),
    ]
