# Generated by Django 2.2.16 on 2021-03-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0016_propiedad_inmueble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='inmueble',
            field=models.BooleanField(default=False, verbose_name='IS_costumer'),
        ),
    ]
