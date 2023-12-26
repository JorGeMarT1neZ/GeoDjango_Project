from django.contrib.gis.db import models
from municipios.models import MunicipiosColombia



class Personas(models.Model):
    sexo_options =(
        ("M","masculino"),
        ("F","femenino")
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 20,blank=False,null=False)
    apellido = models.CharField(max_length = 20,blank=False,null=False)
    sexo = models.CharField(max_length = 8,blank=False,null=False,choices=sexo_options)
    fecha_nacimiento = models.DateField(blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True) #default= timezome.now()-timedelta(hours=5)
    #mun_residencia = models.ForeignKey(MunicipiosColombia,on_delete=models.SET_NULL,related_name= "personas",null=True)
    class Meta:
        db_table = "registro_personas"

