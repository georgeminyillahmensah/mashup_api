from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from .models import Character, Quote, Setting, Genre
from .serializers import CharacterSerializer, QuoteSerializer, SettingSerializer, GenreSerializer
import random

class RandomCharacterView(APIView):
    def get(self, request):
        character = random.choice(Character.objects.all())
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            character = Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            return Response({"error": "Character not found"}, status=HTTP_400_BAD_REQUEST)
        serializer = CharacterSerializer(character, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RandomQuoteView(APIView):
    def get(self, request):
        quote = random.choice(Quote.objects.all())
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            quote = Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            return Response({"error": "Quote not found"}, status=HTTP_400_BAD_REQUEST)
        serializer = QuoteSerializer(quote, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RandomSettingView(APIView):
    def get(self, request):
        setting = random.choice(Setting.objects.all())
        serializer = SettingSerializer(setting)
        return Response(serializer.data)

    def post(self, request):
        serializer = SettingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            setting = Setting.objects.get(pk=pk)
        except Setting.DoesNotExist:
            return Response({"error": "Setting not found"}, status=HTTP_400_BAD_REQUEST)
        serializer = SettingSerializer(setting, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RandomPlotView(APIView):
    def get(self, request):
        genre = random.choice(Genre.objects.all()).name
        character = random.choice(Character.objects.all()).name
        setting = random.choice(Setting.objects.all()).name
        plot = f"In a {genre} story, {character} finds themselves in {setting}."
        return Response({"plot": plot})

    def post(self, request):
        serializer = GenreSerializer(data=request.data)  # Assuming the request creates a new genre for plot generation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
