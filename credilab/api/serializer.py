from rest_framework import serializers
from credilab.models import Client


class ClientSeriliazer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"
