# Generated by Django 3.1.5 on 2021-01-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20210128_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]