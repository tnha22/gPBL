from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.api.models import User, Shift, Log, Face, Camera
from apps.api.serializers import UserSerializer, RegisterSerializer,LoginSerializer, LogSerializer, ShiftSerializer, CameraSerializer

# Class based view to Get User Details using Token Authentication
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetUserShift(APIView):
    def get(self, request, pk):
        shift = Shift.objects.all().filter(user=pk)
        serializer = ShiftSerializer(shift, many=True)
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

class ListCreateShiftView(ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class UpdateDeleteShiftView(RetrieveUpdateDestroyAPIView):
    model = Shift
    serializer_class = ShiftSerializer

    def put(self, request, *args, **kwargs):
        shift = Shift.objects.get(id=kwargs.get('pk'))
        serializer = ShiftSerializer(shift, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Shift successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Shift unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        shift = get_object_or_404(Shift, id=kwargs.get('pk'))
        shift.delete()

        return JsonResponse({
            'message': 'Delete Shift successful!'
        }, status=status.HTTP_200_OK)

class ListCreateCameraView(ListCreateAPIView):
    model = Camera
    serializer_class = CameraSerializer

    def get_queryset(self):
        return Camera.objects.all()

    def post(self, request):
        serializer = CameraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteCameraView(RetrieveUpdateDestroyAPIView):
    model = Camera
    serializer = CameraSerializer

    def get(self, request, *args, **kwargs):
        camera = Camera.objects.get(id=kwargs.get('pk'))
        serializer = CameraSerializer(camera)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        camera = Camera.objects.get(id=kwargs.get('pk'))
        serializer = CameraSerializer(camera, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, *args, **kwargs):
        camera = get_object_or_404(Camera, id=kwargs.get('pk'))
        camera.delete()
        return Response({"status": "success", "data": "Camera Deleted"})


class GetHistoryLog(ListCreateAPIView):
    model = Log
    serializer_class = LogSerializer

    def get_queryset(self):
        return Log.objects.all()







# class FaceDetailView(APIView):
    








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
