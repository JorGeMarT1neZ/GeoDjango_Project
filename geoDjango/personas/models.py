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
    fecha_creacion = models.DateTimeField( """default= timezome.now()-timedelta(hours=5"""  )
    municipio_residencia = models.ForeignKey(MunicipiosColombia,on_delete=models.SET_NULL,null=True,related_name='personas_municipio')
    """Personas.objects.filter(nombre__startswith='p').update"""
    class Meta:
        db_table = "registro_personas"

    def __str__(self):
        return f"{self.nombre}"    
    

animal_op=(("P","perro"),("G","gato"),("C","conejo"),("I","iguana"))


class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    especie = models.CharField(max_length = 20 ,blank=False,null=False,choices=animal_op)
    nombre = models.CharField(max_length = 20 ,blank=False,null=False)
    propietario = models.ForeignKey(Personas,on_delete=models.SET_NULL,null=True,related_name='mascotas')

    class Meta:
        db_table  = 'animal'
        managed = True 
        verbose_name = 'Animal' #
        verbose_name_plural = 'Animales' #


     


