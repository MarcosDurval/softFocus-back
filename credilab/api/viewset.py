from rest_framework import viewsets, status
from rest_framework.response import Response
from credilab.api.serializer import (
    ClientSerializer,
    ClientSerializerEventString
    )
from credilab.api.repository import ClientRepository
from credilab.models import Client


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ClientSerializerEventString
        else:
            return ClientSerializer

    def create(self, request):

        serializer = ClientSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        isValidEvent = ClientRepository.validEvent(self, request)

        if not isValidEvent:
            return Response({"message":
                            "event differs from the already registered"},
                            status=status.HTTP_409_CONFLICT)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):

        instance = self.get_object()
        serializer = ClientSerializer(instance, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        validEvent = ClientRepository.validEvent(self, request, pk)
        if not validEvent:
            return Response({"message":
                            "event differs from the already registered"},
                            status=status.HTTP_409_CONFLICT)

        serializer.save()
        return Response({"message": "update done"},
                        status=status.HTTP_200_OK)
