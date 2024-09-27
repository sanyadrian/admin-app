from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.authentication import JWTAuthentication
from .models import Order
from .serializers import OrderSerializer
from admin.pagination import CustomPagination


class OrderGenericGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                "data": self.retrieve(request, pk).data,
            })
        return self.list(request)
