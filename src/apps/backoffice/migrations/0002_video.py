# Generated by Django 2.2.16 on 2020-10-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titulo del video')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('code', models.TextField(verbose_name='Código del video')),
            ],
        ),
    ]
