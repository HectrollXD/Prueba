# Generated by Django 3.2.1 on 2021-05-11 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Providers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='Provider_Name',
            new_name='provider_name',
        ),
    ]