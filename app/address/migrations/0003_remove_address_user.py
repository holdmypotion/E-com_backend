# Generated by Django 3.0.8 on 2020-07-10 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20200707_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
    ]