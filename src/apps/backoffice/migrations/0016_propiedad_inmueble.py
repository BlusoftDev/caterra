# Generated by Django 2.2.16 on 2021-03-04 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0015_auto_20210304_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='inmueble',
            field=models.BooleanField(default=False, verbose_name='IS costumer'),
        ),
    ]