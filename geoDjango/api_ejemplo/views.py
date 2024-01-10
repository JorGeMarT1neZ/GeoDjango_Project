from rest_framework.generics import ListAPIView
from municipios.models import SubregionesColombia, MunicipiosColombia
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from django.contrib.gis.db.models.functions import Area
from rest_framework.response import Response
from django.db.models.functions import Cast
from django.contrib.gis.db.models import GeometryField , FloatField
from rest_framework.permissions import IsAuthenticated ,AllowAny
from personas.models import Personas
import random
import names
from django.db import connection


# Create your views here.

class consultamunicipiosubregion(ListAPIView):
    serializer_class = minicipios_serializer
    def get_queryset(self):
        nombresub = self.kwargs["nombre"]
        subregion = SubregionesColombia.objects.filter(nom_subreg__iexact=nombresub).first()
        municipios = MunicipiosColombia.objects.filter(geom__coveredby = subregion.geom)
        return municipios


class consultaNombreMunicipios(ListAPIView):
    serializer_class = minicipios_serializer_2
    permission_classes = [IsAuthenticated] # api protegida 
    # permission_classes = [AllowAny] permitir sin auth 
    def get_queryset(self):
        letraMu = self.kwargs["nombre"]  #capturando las letras 
        municipios = MunicipiosColombia.objects.filter(mpio_cnmbr__icontains = letraMu)
        return municipios
    

@api_view(['GET'])
@permission_classes([IsAuthenticated]) # proteccion para la api , protegiendo como funcion 
def consultAreamayor(requets):
    municipios= MunicipiosColombia.objects.annotate(areamun=Cast(Area(Cast('geom', GeometryField(geography=True))),FloatField())).filter(areamun__gte=1000000).order_by("-areamun")[:10]
    respuesta = minicipios_serializer(municipios,many=True).data #pasandole al formato JSON #
    return Response(respuesta)


@api_view(['GET'])
@permission_classes([AllowAny])
def ejecutar_script(requets):
    lista_personas=[
        {"nombre":"Carlos",
         "apellido":"Diaz",
         "fecha_nacimiento":"1996-06-15",
         "sexo":"M",
         "municipio_residencia":"1112"}
    ]
    try:
        lista_municipios = list(MunicipiosColombia.objects.all())
        lista_personas = []
        def buscar_municipios(id_municipio):
            for municipio in lista_municipios:
                if municipio.id == id_municipio :
                    return municipio
            return None

        for i in range(10000):
            listnum = random.randint(1,1118)
            mi_persona = Personas(
                nombre= f'pepito {i+1}',
                apellido= f'Perez {i+1}',
                sexo= 'M',
                fecha_nacimiento= "1996-06-15",
                municipio_residencia = buscar_municipios(listnum),
            )

            lista_personas.append(mi_persona)

        #bulk create -  carga masiva 
        Personas.objects.bulk_create(lista_personas,batch_size=1000)
        return Response({"mensaje_ejecuto":False})       

    except Exception as e:
        return Response({"mensaje_ejecuto":False,"excepcion":str(e)})
    

@api_view(['GET'])
@permission_classes([AllowAny])
def actualizar_script(requets):

    with connection.cursor() as cursor:
        for i in range(10000):
            fecha = f'{random.randrange(1990,2010)}-{random.randrange(1,12)}-{random.randrange(1,30)}'
            nombre = names.get_first_name()
            ape =  names.get_last_name()
            _sexo = 'M'
            cursor.execute("UPDATE django.registro_personas SET nombre=%s, apellido=%s, sexo=%s, fecha_nacimiento=%s WHERE id=%s;",[nombre,ape,_sexo,fecha,i])
    return Response({"mensaje":True})
    

@api_view(['GET'])
@permission_classes([AllowAny])
def letter_m(requets):
    #people = Personas.objects.raw("select id, nombre, apellido, sexo, fecha_nacimiento, fecha_creacion, municipio_residencia_id from django.registro_personas limit 100;")
    #people = Personas.objects.all().select_related("municipio_residencia")[:100] #limitar la consulta a 100 , mas rapido
    people = Personas.objects.prefetch_related("municipio_residencia").all()[:100] #  precargar los datos 
     
    respuesta = personas_serialaizer(people,many=True).data
    return Response(respuesta)