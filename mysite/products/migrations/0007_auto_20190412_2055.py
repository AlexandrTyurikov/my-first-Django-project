# Generated by Django 2.2 on 2019-04-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190412_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='publishing',
            field=models.ManyToManyField(to='products.Publishing', verbose_name='Издательство'),
        ),
    ]