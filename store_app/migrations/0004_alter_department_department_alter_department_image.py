# Generated by Django 4.2.5 on 2024-01-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_department_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]