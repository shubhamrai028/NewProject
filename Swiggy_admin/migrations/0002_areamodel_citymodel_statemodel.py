# Generated by Django 2.2.5 on 2020-04-16 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Swiggy_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('state_no', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('city_no', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Swiggy_admin.StateModel')),
            ],
        ),
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('area_no', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Swiggy_admin.CityModel')),
            ],
        ),
    ]