# Generated by Django 4.2.5 on 2024-01-13 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_alter_department_options_department_wiki_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='wiki_link',
        ),
    ]
