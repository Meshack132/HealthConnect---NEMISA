# Generated by Django 3.0.3 on 2023-11-19 01:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('registration_no', models.CharField(max_length=20)),
                ('year_of_registration', models.DateField()),
                ('qualification', models.CharField(max_length=20)),
                ('State_Medical_Council', models.CharField(max_length=30)),
                ('specialization', models.CharField(max_length=30)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_patient', models.BooleanField(default=True)),
                ('is_doctor', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='public_post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_header', models.CharField(max_length=250)),
                ('post_text', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(db_column='user', default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('post', models.ForeignKey(db_column='post', on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main_app.public_post')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='main_app.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='rating_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('review', models.TextField(blank=True)),
                ('doctor', models.ForeignKey(db_column='doctor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.doctor')),
                ('patient', models.ForeignKey(db_column='patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='diseaseinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseasename', models.CharField(max_length=200)),
                ('no_of_symp', models.IntegerField()),
                ('symptomsname', models.TextField()),
                ('confidence', models.DecimalField(decimal_places=2, max_digits=5)),
                ('consultdoctor', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(db_column='patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('diseaseinfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.diseaseinfo')),
                ('doctor', models.ForeignKey(db_column='doctor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.doctor')),
                ('patient', models.ForeignKey(db_column='patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.patient')),
            ],
        ),
    ]
