# Generated by Django 2.2.16 on 2021-03-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0006_agente_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Dirección'),
        ),
    ]