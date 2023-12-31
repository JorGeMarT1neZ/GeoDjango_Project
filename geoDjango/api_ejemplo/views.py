from rest_framework.generics import ListAPIView
from municipios.models import SubregionesColombia, MunicipiosColombia
from .serializers import *
from rest_framework.decorators import api_view
from django.contrib.gis.db.models.functions import Area
from rest_framework.response import Response
from django.db.models.functions import Cast
from django.contrib.gis.db.models import GeometryField

# Create your views here.

class consultamunicipiosubregion(ListAPIView):
    serializer_class= minicipios_serializer
    def get_queryset(self):
        nombresub = self.kwargs["nombre"]
        subregion = SubregionesColombia.objects.filter(nom_subreg__iexact=nombresub).first()
        municipios = MunicipiosColombia.objects.filter(geom__coveredby = subregion.geom)

        return municipios


class consultaNombreMunicipios(ListAPIView):
    serializer_class = minicipios_serializer_2
    def get_queryset(self):
        letraMu = self.kwargs["nombre"]  #capturando las letras 
        municipios = MunicipiosColombia.objects.filter(mpio_cnmbr__icontains = letraMu)
        return municipios
    

@api_view(['GET'])
def consultAreamayor(requets):
    municipios= MunicipiosColombia.objects.annotate(areamun=Area(Cast('geom', GeometryField(geography=True)))).filter(areamun__gte=10000)
    respuesta = minicipios_serializer_2(municipios,many=True).data #pasandole al formato JSON #
    return Response(respuesta)