from credilab.models import Client
from haversine import haversine


class ClientRepository:
    def validEvent(self, request, pk=None):
        request_client = request.data
        clients = Client.objects.filter(date=request_client["date"])
        if not len(clients):
            return True
        request_client_id = pk
        latitude = float(request_client["latitude"])
        longitude = float(request_client["longitude"])
        for client in clients:
            client_lat = float(client.latitude)
            client_long = float(client.longitude)
            dist = haversine((client_lat, client_long), (latitude, longitude))
            if dist <= 10 and client.event != request_client["event"]:
                if request_client_id != client.id:
                    return False
        return True
