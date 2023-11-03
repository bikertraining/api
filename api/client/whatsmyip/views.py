from ipware.ip import get_client_ip
from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class Index(views.APIView):
    """
    What is my IP Address
    """

    permission_classes = (
        AllowAny,
    )

    @staticmethod
    def get(request):
        ip = get_client_ip(request)

        return Response(ip[0])
