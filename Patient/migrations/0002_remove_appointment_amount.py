# Generated by Django 3.1.1 on 2021-02-08 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='amount',
        ),
    ]
