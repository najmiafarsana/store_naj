# Generated by Django 4.2.5 on 2024-01-11 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='name',
        ),
    ]
