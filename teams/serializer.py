
from rest_framework import serializers
from .models import Team
#que datos seran seleccionanos para enviarlos del backen en json para el front

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model= Team
    # fields=("id", "nombre" "capitan", "descripcion", "jugadores", "activo")
        fields= '__all__' #serializar todo