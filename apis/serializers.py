from rest_framework import serializers

from .models import OperationFact

class OperationFactSerialezer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'created',
      'modified',
      'body',
    )
    model = OperationFact