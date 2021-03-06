# Generated by Django 2.2.16 on 2021-03-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0024_auto_20210304_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='captada_por',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='clave',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='colonia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='construccion',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='cp',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='entre_calle_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='entre_calle_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='estado',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='fondo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='frente',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='propiedades'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='mantenimiento_mensual',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='moneda',
            field=models.CharField(blank=True, choices=[('MN', 'MN'), ('DOLARES', 'Dólares')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='precio',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='terreno',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
