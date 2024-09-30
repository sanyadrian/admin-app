from django.urls import path
from .views import OrderGenericGenericAPIView, ExportAPIView, ChartAPIView


urlpatterns = [
    path("orders", OrderGenericGenericAPIView.as_view()),
    path("orders/<str:pk>", OrderGenericGenericAPIView.as_view()),
    path("export", ExportAPIView.as_view()),
    path("chart", ChartAPIView.as_view())
]
