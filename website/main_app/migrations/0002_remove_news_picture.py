# Generated by Django 3.2.12 on 2022-03-21 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='picture',
        ),
    ]
