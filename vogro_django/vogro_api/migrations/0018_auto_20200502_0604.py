# Generated by Django 3.0.5 on 2020-05-02 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vogro_api', '0017_auto_20200502_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedgrocerypost',
            name='time_of_post',
        ),
        migrations.RemoveField(
            model_name='livegrocerypost',
            name='time_of_post',
        ),
    ]