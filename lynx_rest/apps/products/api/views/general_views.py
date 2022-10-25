from apps.products.api.serializers.general_serializers import (
    CategoryProductSerializer, IndicatorSerializer, MeasureUnitSerializer)
from apps.products.models import CategoryProduct, Indicator, MeasureUnit
from rest_framework import generics


class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        MeasureUnit.objects.filter(state=True)


class IndicatortListAPIView(generics.ListAPIView):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        Indicator.objects.filter(state=True)


class CategoryProducttListAPIView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        CategoryProduct.objects.filter(state=True)
