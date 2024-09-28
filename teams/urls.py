from django.urls import path, include
from rest_framework import routers #me va a generar todas las url de la vista
from . import views


router= routers.DefaultRouter()
router.register(r'teams', views.TeamView, 'teams' ) #registrando un nueva ruta basada en la vista 


urlpatterns = [
    path("api/" , include(router.urls)) #tiodo lo generado por router y quiero esas urls 
]

#va a generar las rutas get post  put delete