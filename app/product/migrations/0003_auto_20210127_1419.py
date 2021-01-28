# Generated by Django 3.1.5 on 2021-01-27 08:49

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201229_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.get_image_filename, verbose_name='Image1'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.get_image_filename, verbose_name='Image2'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.get_image_filename, verbose_name='Image3'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.get_image_filename, verbose_name='Image4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]