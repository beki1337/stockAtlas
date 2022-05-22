from predictions.models import Predictions
from rest_framework import serializers
class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = ['ticket','date','price','diraction']
