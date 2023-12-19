from municipios.models import MunicipiosColombia
from rest_framework import serializers
from rest_framework_gis.serializers import  GeoFeatureModelSerializer
from rest_framework.serializers import SerializerMethodField


                                   #geojson#
class minicipios_serializer(GeoFeatureModelSerializer):
    class Meta:
        model = MunicipiosColombia
        geo_field = "geom"
        fields = ('__all__')

                                  #alfanumerico#
class minicipios_serializer_2(serializers.ModelSerializer):
    area = SerializerMethodField('get_area')
    def get_area(self,object):
        try:
            return object.areamun
        except:
            return None
    class Meta:
        model = MunicipiosColombia
        fields = ('mpio_cnmbr','descrpcion','depto','geom','area')