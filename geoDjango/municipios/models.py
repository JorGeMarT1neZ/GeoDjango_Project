from django.db import models

from django.contrib.gis.db import models


class MunicipiosColombia(models.Model):
    #id = models.AutoField(primary_key=True,unique=True)
    id = models.IntegerField(primary_key=True,unique=True)
    geom = models.MultiPolygonField(srid=4326,blank=True, null=True)
    objectid_1 = models.IntegerField(blank=True, null=True)
    dpto_ccdgo = models.CharField(max_length=2, blank=True, null=True)
    mpio_ccdgo = models.CharField(max_length=3, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    objectid = models.IntegerField()
    mpio_cnmbr = models.CharField(max_length=28, blank=True, null=True)
    descrpcion = models.CharField(max_length=12, blank=True, null=True)
    depto = models.CharField(max_length=39, blank=True, null=True)
    p_enersi = models.IntegerField(blank=True, null=True)
    p_enerno = models.IntegerField(blank=True, null=True)
    p_alcansi = models.IntegerField(blank=True, null=True)
    p_alcanno = models.IntegerField(blank=True, null=True)
    p_acuesi = models.IntegerField(blank=True, null=True)
    p_acueno = models.IntegerField(blank=True, null=True)
    p_gasnsi = models.IntegerField(blank=True, null=True)
    p_gasnno = models.IntegerField(blank=True, null=True)
    p_gasnnoin = models.IntegerField(blank=True, null=True)
    p_telefsi = models.IntegerField(blank=True, null=True)
    p_telefno = models.IntegerField(blank=True, null=True)
    p_telefnoi = models.IntegerField(blank=True, null=True)
    shapestare = models.FloatField(blank=True, null=True)
    shapestlen = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios_colombia'

    def __str__(self):
        return f"{self.mpio_cnmbr}"


class SubregionesColombia(models.Model):
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)
    objectid = models.IntegerField(primary_key=True)
    cod_subreg = models.CharField(max_length=4, blank=True, null=True)
    nom_subreg = models.CharField(max_length=27, blank=True, null=True)
    cod_depto = models.CharField(max_length=2, blank=True, null=True)
    shapestare = models.FloatField(blank=True, null=True)
    shapestlen = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subregiones_colombia'


    def __str__(self):
        return f"{self.nom_subreg}"
