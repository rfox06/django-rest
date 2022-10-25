from apps.products.api.views.general_views import (CategoryProducttListAPIView,
                                                   IndicatortListAPIView,
                                                   MeasureUnitListAPIView)
from django.urls import path

urlpatterns = [
    path('measure_unit/',
         MeasureUnitListAPIView.as_view(),
         name='measure_unit'
         ),
    path('indicator/',
         IndicatortListAPIView.as_view(),
         name='indicator'
         ),
    path('category_product/',
         CategoryProducttListAPIView.as_view(),
         name='category_product'
         ),

]
