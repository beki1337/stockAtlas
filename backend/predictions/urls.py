from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from predictions import views


urlpatterns = [
    path('predictions/',views.PredictionsList.as_view()),
    path('predictions/<int:pk>',views.PredictionsDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
