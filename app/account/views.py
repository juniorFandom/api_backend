from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, MyTokenObtaiTokenSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView
from .models import User



class RegisterView(GenericAPIView, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtaiTokenSerializer
    permission_classes = [AllowAny]


class testView(GenericAPIView, ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Hello, World!'})
# Create your views here.
