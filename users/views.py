from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions
from .models import User
from .serializers import UserSerializer
from .authentication import generate_access_token


@api_view(["POST"])
def register(request):
    data=request.data
    if data["password"] != data["password_confirm"]:
        raise exceptions.APIException("Password do not match!")
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed("User not Found")
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Incorrect Password!")
 
    response = Response()
    token = generate_access_token(user)
    response.set_cookie(key="jwt", value=token, httponly=True)
    response.data = {
        "jwt": token
    }
    return response


@api_view(["GET"])
def users(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)
