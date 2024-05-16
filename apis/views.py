from datetime import datetime
from rest_framework import generics
from django_filters import rest_framework as filters
from .filters import DateFilter

from .models import OperationFact
from .serializers import OperationFactSerialezer


class OperationFactList(generics.ListCreateAPIView):
  queryset = OperationFact.objects.all()
  serializer_class = OperationFactSerialezer

class OperationFactGteList(generics.ListCreateAPIView):
  queryset = OperationFact.objects.all()
  serializer_class = OperationFactSerialezer
  filter_backends = (filters.DjangoFilterBackend,)
  filterset_class = DateFilter
