# Generated by Django 3.2.23 on 2024-01-02 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='add',
            new_name='message',
        ),
    ]
