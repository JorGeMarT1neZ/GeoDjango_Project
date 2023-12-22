from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    
    path("municipiosregion/<nombre>", consultamunicipiosubregion.as_view()),
    path("municipiosLetra/<nombre>", consultaNombreMunicipios.as_view()),
    path("municipios_area/",consultAreamayor),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

