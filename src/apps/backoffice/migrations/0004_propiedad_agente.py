# Generated by Django 2.2.16 on 2021-03-10 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('backoffice', '0003_remove_propiedad_agente'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='agente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.Agente'),
        ),
    ]