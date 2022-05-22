from django.shortcuts import render

# Create your views here.
from predictions.models import Predictions
from predictions.serializers import PredictionSerializer
from rest_framework import generics


class PredictionsList(generics.ListCreateAPIView):
    queryset = Predictions.objects.filter(activ=True)
    serializer_class = PredictionSerializer

class PredictionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Predictions.objects.all()
    serializer_class = PredictionSerializer
