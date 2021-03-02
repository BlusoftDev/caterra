# Generated by Django 2.2.16 on 2021-03-02 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210301_1733'),
        ('backoffice', '0007_delete_agente'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='agente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Agente'),
        ),
    ]
