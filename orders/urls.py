from django.urls import path
from .views import OrderGenericGenericAPIView


urlpatterns = [
    path("orders", OrderGenericGenericAPIView.as_view()),
    path("orders/<str:pk>", OrderGenericGenericAPIView.as_view()),
]
