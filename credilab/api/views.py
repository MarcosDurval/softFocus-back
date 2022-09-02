from rest_framework import viewsets
from credilab.api.serializer import ClientSeriliazer

from credilab.models import Client


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSeriliazer
