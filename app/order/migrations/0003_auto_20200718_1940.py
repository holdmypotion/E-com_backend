# Generated by Django 3.0.8 on 2020-07-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200718_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.SlugField(max_length=120, primary_key=True, serialize=False),
        ),
    ]
