# Generated by Django 3.2.1 on 2021-05-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='secondname',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
