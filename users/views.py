from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from users.serializers import SignUpSerializer, SignInSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate

class SignUpView(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "сообщение": "пользователя успешно зареган",
                "data": {"username": serializer.data.get("username"),
                         "email": serializer.data.get("email")}
            }
            return Response(data=response)

class SignInView(APIView):
    serializer_class = SignInSerializer

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken().for_user(user)
            response = {
                "сообщение": "Вы успешно вошли в систему",
                "tokens": {
                    "refersh": str(refresh),
                    "access": str(refresh.access_token),
                },
                "user": user.username,
            }
            return Response(data=response)
        else:
            return Response(data={"вы не вошли в систему"})


# Create your views here.
