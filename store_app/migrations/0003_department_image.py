# Generated by Django 4.2.5 on 2024-01-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_remove_department_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]