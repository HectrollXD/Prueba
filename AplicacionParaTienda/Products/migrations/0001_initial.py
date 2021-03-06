# Generated by Django 3.2.1 on 2021-05-14 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Providers', '0001_initial'),
        ('Departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=150)),
                ('productdescription', models.CharField(blank=True, max_length=500, null=True)),
                ('productid', models.CharField(max_length=50)),
                ('productprice', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Departments.department')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Providers.provider')),
            ],
        ),
    ]
