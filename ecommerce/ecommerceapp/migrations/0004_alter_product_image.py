# Generated by Django 4.2.4 on 2023-08-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_alter_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
