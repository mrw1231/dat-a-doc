# Generated by Django 3.2.9 on 2022-01-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
