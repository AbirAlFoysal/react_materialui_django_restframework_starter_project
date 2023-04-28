from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class CrudTable(APIView):
    def get(self, request):
        crudObj = Crud.objects.all()
        crudSerializer = CrudSerializer(crudObj, many=True)
        return Response(crudSerializer.data)

    def post(self, request):
        crudSerializer = CrudSerializer(data=request.data)
        if crudSerializer.is_valid():
            crudSerializer.save()
            return Response(crudSerializer.data)
        return Response(crudSerializer.errors)

class CrudTableUpdate(APIView):
    def get(self, request, pk):
        crudObj = Crud.objects.get(id=pk)
        crudSerializer = CrudSerializer(crudObj)
        return Response(crudSerializer.data)

    def put(self, request, pk):
        crudObj = Crud.objects.get(id=pk)
        crudSerializer = CrudSerializer(crudObj, data=request.data)
        if crudSerializer.is_valid():
            crudSerializer.save()
            return Response(crudSerializer.data)
        return Response(crudSerializer.errors)

    def delete(self, request, pk):
        crudObj = Crud.objects.get(id=pk)
        crudObj.delete()
        return Response("Item deleted successfully")