# Generated by Django 2.0.7 on 2019-07-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190727_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('treats', 'treats'), ('appetizers', 'appetizers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
