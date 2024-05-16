from django.contrib import admin

from .models import OperationFact, TblForWrite

@admin.register(OperationFact)
class OperationFactAdmin(admin.ModelAdmin):
  list_display = ['id', 'created', 'modified', 'body']

@admin.register(TblForWrite)
class OperationFactAdmin(admin.ModelAdmin):
  list_display = ['id', 'wr_id', 'wr_created', 'wr_modified', 'wr_body']
