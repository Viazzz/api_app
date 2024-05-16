from django.urls import path

from .views import OperationFactList, OperationFactGteList


urlpatterns = [
    path('', OperationFactGteList.as_view(), name='operation_fact_list')
]
