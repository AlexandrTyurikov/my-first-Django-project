# Generated by Django 2.2 on 2019-04-09 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Обложка'),
        ),
    ]
