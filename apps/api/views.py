from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.api.models import User
from apps.api.serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id = request.user.id)
        serializer = UserSerializer(user)

        return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginUserView(APIView):

    # Define methods
    model = User
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }
                return Response(data, status=status.HTTP_200_OK)

            return Response({
                'error_message': 'Username or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)

# blog/views.py







'''
class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)

class CreateUserView(APIView):

    # Define methods
    model = User
    serializer_class = UserSerializer

    def post(self, request, format=None, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': "Create successfully"
            }, status=status.HTTP_201_CREATED)
        
        return JsonResponse({
            'message': "Create unsuccessfully"
        }, status=status.HTTP_400_BAD_REQUEST)

class ListUserView(ListCreateAPIView):
    # Define methods
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, format=None, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': "Create successfully"
            }, status=status.HTTP_201_CREATED)
        

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    # Define methods
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def put(self, request, format=None, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('pk'))
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': "Update successfully"
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('pk'))
        user.delete()

        return JsonResponse({
            'message': "Delete successfully"
        }, status=status.HTTP_200_OK)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''
