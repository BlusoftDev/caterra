# Generated by Django 2.2.16 on 2021-03-04 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0010_propiedad0'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Propiedad0',
        ),
        migrations.RemoveField(
            model_name='propiedad',
            name='imagen',
        ),
        migrations.AddField(
            model_name='propiedad',
            name='inmueble',
            field=models.BooleanField(default='false'),
        ),
    ]