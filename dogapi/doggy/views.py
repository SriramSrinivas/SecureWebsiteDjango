# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from doggy.models import dog,breed

from doggy.serializers import dogSerializer 
from doggy.BreedSerializers import breedSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
# Create your views here.
from rest_framework import status
# @csrf_exempt
class dogList(APIView):
    def get(self, request, format=None):
        snippets = dog.objects.all()
        serializer = dogSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = dogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class breedList(APIView):
    def get(self, request, format=None):
        snippets = breed.objects.all()
        serializer = breedSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = breedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    """
    Retrieve, update or delete a dog instance.
    """
    def get_object(self, pk):
        try:
            return dog.objects.get(pk=pk)
        except dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dog= self.get_object(pk)
        serializer = dogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dog= self.get_object(pk)
        serializer = dogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BreedDetail(APIView):
    """
    Retrieve, update or delete a dog instance.
    """
    def get_object(self, pk):
        try:
            return breed.objects.get(pk=pk)
        except dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        breed= self.get_object(pk)
        serializer = breedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        breed= self.get_object(pk)
        serializer = breedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        breed= self.get_object(pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)