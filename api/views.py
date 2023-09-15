from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TodoSerializers, Todo
# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing todo
    """

    serializer_class = TodoSerializers
    queryset = Todo.objects.all()