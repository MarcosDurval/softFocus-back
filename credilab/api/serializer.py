from rest_framework import serializers
from credilab.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def validate(self, data):
        latitude = data["latitude"]
        longitude = data["longitude"]

        if not ((-90 <= latitude <= 90) or (-180 <= longitude <= 180)):
            raise serializers.ValidationError("Invalid latitude or longitude")
        return data


class ClientSerializerEventString(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = "__all__"

    def get_event(self, obj):
        return obj.get_event_display()
