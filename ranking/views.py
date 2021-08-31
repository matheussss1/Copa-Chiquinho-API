from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JogadorSerializer

from django.http import FileResponse

from .models import Jogador

@api_view(['GET'])
def show_ranking(request):
    ranking = Jogador.objects.all()
    serializer = JogadorSerializer(ranking, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def show_image(request, player, filename):
#     path = f'upload/player_teste/download.jpg'
#     img = open(path)
#     return FileResponse(img)