from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Video
from . serializers import VideoSerializer

# Create your views here.

@api_view(['GET'])
def video_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)