# Generated by Django 4.0.4 on 2022-05-28 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_size_product_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['ordering'], 'verbose_name_plural': 'categories'},
        ),
    ]
