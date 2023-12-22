# Generated by Django 4.2 on 2023-12-22 02:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipiosColombia',
            fields=[
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('objectid_1', models.IntegerField(blank=True, null=True)),
                ('dpto_ccdgo', models.CharField(blank=True, max_length=2, null=True)),
                ('mpio_ccdgo', models.CharField(blank=True, max_length=3, null=True)),
                ('shape_leng', models.FloatField(blank=True, null=True)),
                ('objectid', models.IntegerField(primary_key=True, serialize=False)),
                ('mpio_cnmbr', models.CharField(blank=True, max_length=28, null=True)),
                ('descrpcion', models.CharField(blank=True, max_length=12, null=True)),
                ('depto', models.CharField(blank=True, max_length=39, null=True)),
                ('p_enersi', models.IntegerField(blank=True, null=True)),
                ('p_enerno', models.IntegerField(blank=True, null=True)),
                ('p_alcansi', models.IntegerField(blank=True, null=True)),
                ('p_alcanno', models.IntegerField(blank=True, null=True)),
                ('p_acuesi', models.IntegerField(blank=True, null=True)),
                ('p_acueno', models.IntegerField(blank=True, null=True)),
                ('p_gasnsi', models.IntegerField(blank=True, null=True)),
                ('p_gasnno', models.IntegerField(blank=True, null=True)),
                ('p_gasnnoin', models.IntegerField(blank=True, null=True)),
                ('p_telefsi', models.IntegerField(blank=True, null=True)),
                ('p_telefno', models.IntegerField(blank=True, null=True)),
                ('p_telefnoi', models.IntegerField(blank=True, null=True)),
                ('shapestare', models.FloatField(blank=True, null=True)),
                ('shapestlen', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'municipios_colombia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubregionesColombia',
            fields=[
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('objectid', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_subreg', models.CharField(blank=True, max_length=4, null=True)),
                ('nom_subreg', models.CharField(blank=True, max_length=27, null=True)),
                ('cod_depto', models.CharField(blank=True, max_length=2, null=True)),
                ('shapestare', models.FloatField(blank=True, null=True)),
                ('shapestlen', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'subregiones_colombia',
                'managed': False,
            },
        ),
    ]