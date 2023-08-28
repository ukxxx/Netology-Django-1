from django.urls import path
from measurement.views import *

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<int:pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<int:pk>/details/', SensorDetailView.as_view()),
]
