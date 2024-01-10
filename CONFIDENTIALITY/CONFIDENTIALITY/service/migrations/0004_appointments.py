# Generated by Django 3.2.23 on 2024-01-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('phoneNo', models.CharField(max_length=15)),
                ('appointmentDate', models.DateField()),
                ('symptoms', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]