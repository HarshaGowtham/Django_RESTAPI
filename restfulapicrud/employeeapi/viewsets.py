from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    # queryset = models.Employee.objects.all() - to retrieve all the records
    queryset = models.Employee.objects.filter(deleted ="1")  #to retrieve the table without delted and updated records
    #queryset = models.Employee.objects.filter(deleted="1") - to retrieve deleted records
    #queryset = models.Employee.objects.filter(deleted="2") - to retrieve updated records
    #queryset = models.Employee.objects.filter(deleted != "1") - to retrieve the data except the deleted records
    serializer_class = serializers.EmployeSerializer


#list() retrieve()  create() update() destroy()