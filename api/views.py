from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from .models import Character, Quote, Setting, Genre
from .serializers import CharacterSerializer, QuoteSerializer, SettingSerializer, GenreSerializer
import random


# Character View
class CharacterView(ListCreateAPIView, RetrieveUpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get(self, request, *args, **kwargs):
        if 'random' in request.query_params:
            character = random.choice(self.get_queryset())
            serializer = self.serializer_class(character)
            return Response(serializer.data)
        return super().get(request, *args, **kwargs)


# Quote View
class QuoteView(ListCreateAPIView, RetrieveUpdateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request, *args, **kwargs):
        if 'random' in request.query_params:
            quote = random.choice(self.get_queryset())
            serializer = self.serializer_class(quote)
            return Response(serializer.data)
        return super().get(request, *args, **kwargs)


# Setting View
class SettingView(ListCreateAPIView, RetrieveUpdateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

    def get(self, request, *args, **kwargs):
        if 'random' in request.query_params:
            setting = random.choice(self.get_queryset())
            serializer = self.serializer_class(setting)
            return Response(serializer.data)
        return super().get(request, *args, **kwargs)


# Genre View (Plot Generator)
class RandomPlotView(APIView):
    def get(self, request):
        genre = random.choice(Genre.objects.all()).name
        character = random.choice(Character.objects.all()).name
        setting = random.choice(Setting.objects.all()).name
        plot = f"In a {genre} story, {character} finds themselves in {setting}."
        return Response({"plot": plot})

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
