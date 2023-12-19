from django.contrib import admin
from django.urls import path,include
from api_ejemplo import urls as api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(api))
]

