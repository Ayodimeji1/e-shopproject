# Generated by Django 4.0.4 on 2022-05-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_image_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('Sale', 'Sale'), ('In Stock', 'In Stock')], default='In Stock', max_length=100),
        ),
    ]
