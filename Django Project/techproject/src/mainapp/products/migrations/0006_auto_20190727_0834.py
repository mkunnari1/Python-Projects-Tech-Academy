# Generated by Django 2.0.7 on 2019-07-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190725_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
