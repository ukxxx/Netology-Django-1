from rest_framework.routers import DefaultRouter
from django.urls import path, include

from logistic.views import ProductViewSet, StockViewSet, sample_view

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("stocks", StockViewSet)

urlpatterns = [
    path("api/v1/test/", sample_view),
    path("api/v1/", include(router.urls)),
]
