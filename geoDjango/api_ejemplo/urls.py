from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    
    path("municipiosregion/<nombre>", consultamunicipiosubregion.as_view()),
    path("municipiosLetra/<nombre>", consultaNombreMunicipios.as_view()),
    path("municipios_area/",consultAreamayor),

    #Este endpoint se utiliza para obtener un par de tokens de acceso y de actualización. 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #Este endpoint se utiliza para refrescar un token de acceso. Cuando el token de acceso expira, el 
    #cliente puede enviar el token de actualización al /token/refresh/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Este endpoint permite verificar la validez de un token. Un cliente puede enviar un token 
    # al /token/verify/ para verificar si es válido o no. Esta ruta es útil para validar tokens 
    # antes de realizar acciones sensibles o para comprobar si un token sigue siendo válido.
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('ejecutar_script/',ejecutar_script),
    path('upscript/',actualizar_script),
    path('letterm/',letter_m),
]

