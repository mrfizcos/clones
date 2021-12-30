# Generated by Django 3.1.4 on 2021-12-15 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upazilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.district')),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.district')),
                ('upazilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.upazilla')),
            ],
        ),
    ]
