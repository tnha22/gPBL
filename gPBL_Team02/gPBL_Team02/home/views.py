from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from home.models import Person
from home.serializers import PersonSerializer, PersonPortalSerializer

class CreatePersonView(APIView):

    # Define methods
    model = Person
    serializer_class = PersonSerializer

    def post(self, request, format=None, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': "Create successfully"
            }, status=status.HTTP_201_CREATED)
        
        return JsonResponse({
            'message': "Create unsuccessfully"
        }, status=status.HTTP_400_BAD_REQUEST)

class ListPersonView(ListCreateAPIView):
    # Define methods
    model = Person
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

    def post(self, request, format=None, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': "Create successfully"
            }, status=status.HTTP_201_CREATED)
        
        return JsonResponse({
            'message': "Create unsuccessfully"
        }, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateDeletePersonView(RetrieveUpdateDestroyAPIView):
    # Define methods
    model = Person
    serializer_class = PersonSerializer

    def put(self, request, format=None, *args, **kwargs):
        person = get_object_or_404(Person, id=kwargs.get('pk'))
        serializer = PersonSerializer(person, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': "Update successfully"
            }, status=status.HTTP_200_OK)
        
        return JsonResponse({
            'message': "Update unsuccessfully"
        }, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, *args, **kwargs):
        person = get_object_or_404(Person, id=kwargs.get('pk'))
        person.delete()

        return JsonResponse({
            'message': "Delete successfully"
        }, status=status.HTTP_200_OK)

# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer