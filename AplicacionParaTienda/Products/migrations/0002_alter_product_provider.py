# Generated by Django 3.2.1 on 2021-05-11 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Providers', '0001_initial'),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Providers.provider', verbose_name='Privider_Name'),
        ),
    ]