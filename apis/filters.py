import django_filters 
from .models import OperationFact


class DateFilter(django_filters.FilterSet):
  class Meta:
    model = OperationFact
    fields = {
      'modified':['gte']
    }