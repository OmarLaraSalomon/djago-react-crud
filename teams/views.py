from rest_framework import viewsets
from .serializer import TeamSerializer
from .models import Team
# Create your views here.


#con una sola clase creamos el crud
class TeamView(viewsets.ModelViewSet) : #bnos va permitir extender
    #ejecuta esete serializer
    serializer_class= TeamSerializer #que traiga la clase 
    queryset= Team.objects.all() #traigo todos los equipos