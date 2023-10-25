# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Measurement, Sensor
from measurement.serializers import (
    SensorSerializer,
    MeasurementSerializer,
    SensorDetailSerializer,
)


# 1. Создать датчик. Указываются название и описание датчика.
class SensorCreateView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_queryset(self):
        return Sensor.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)


# 2. Изменить датчик. Указываются название и описание.
class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# 3. Добавить измерение. Указываются ID датчика и температура.
class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# 4. Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request):
        return Response(SensorSerializer(self.queryset, many=True).data)


# 5. Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.
class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
