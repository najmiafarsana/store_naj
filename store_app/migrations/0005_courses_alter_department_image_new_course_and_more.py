# Generated by Django 4.2.5 on 2024-01-12 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_alter_department_department_alter_department_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(upload_to='department'),
        ),
        migrations.CreateModel(
            name='new_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_app.courses')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_app.department')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.department'),
        ),
    ]