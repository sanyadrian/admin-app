from django.urls import path
from .views import OrderGenericGenericAPIView, ExportAPIView


urlpatterns = [
    path("orders", OrderGenericGenericAPIView.as_view()),
    path("orders/<str:pk>", OrderGenericGenericAPIView.as_view()),
    path("export", ExportAPIView.as_view())
]
