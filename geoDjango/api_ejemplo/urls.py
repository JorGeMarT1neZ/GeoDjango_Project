from django.urls import path
from .views import *

urlpatterns = [
    path("municipiosregion/<nombre>", consultamunicipiosubregion.as_view()),
    path("municipiosLetra/<nombre>", consultaNombreMunicipios.as_view()),
    path("municipios_area/",consultAreamayor)
    
]

