# Generated by Django 4.2 on 2023-12-28 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipios', '0001_initial'),
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='municipio_residencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personas_municipio', to='municipios.municipioscolombia'),
        ),
    ]
