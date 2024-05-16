from django.db import models


class OperationFact(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  body = models.TextField()


class TblForWrite(models.Model):
  wr_id = models.IntegerField()
  wr_created = models.DateTimeField()
  wr_modified = models.DateTimeField()
  wr_body = models.TextField()
  
