from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from admin.fraud import models
from admin.fraud import serializers


class Choices(views.APIView):
    """
    The Choices class is an API view that provides a list of choices for the FraudString Type.
    It inherits from views.APIView and is used for retrieving the choices.

    Permission Classes:
    - IsAdminUser: Only admin users are allowed to access this API view.

    Methods:
    - get(self, request):
        This method handles the GET request to retrieve the list of choices.

        Parameters:
        - request: The request object.

        Return type:
        - Response: The response containing the dictionary of choices.
    """

    permission_classes = (
        IsAdminUser,
    )

    def get(self, request):
        """
        Get method to retrieve the choices of FraudString Type.

        Parameters:
        - request: HttpRequest object representing the incoming request.

        Returns:
        - Response object containing a dictionary of the FraudString Type choices.
        """

        return Response(dict(models.FraudString.Type.choices))


class Create(generics.CreateAPIView):
    """
    Class Create

    This class is a generic API view designed for creating instances of the FraudString model.

    Attributes:
    - permission_classes: A tuple containing the permission classes to be applied to the view.
                          In this case, only admin users are allowed to access this view.
    - queryset: A QuerySet containing all the instances of the FraudString model.
    - serializer_class: The serializer class used for serializing and deserializing instances of the FraudString model.
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.FraudString.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.RetrieveDestroyAPIView):
    """
    This class represents an API view for deleting instances of `models.FraudString`.

    It extends the `generics.RetrieveDestroyAPIView` class from the `rest_framework` module.

    Attributes:
        permission_classes (tuple): A tuple containing the `IsAdminUser` permission class to restrict access
                                    to only admin users.
        queryset (QuerySet): A QuerySet containing all instances of `models.FraudString` to be deleted.
        serializer_class (Serializer): The serializer class to be used for serializing and deserializing
                                       instances of `models.FraudString`.
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.FraudString.objects.all()

    serializer_class = serializers.SearchSerializer


class Edit(generics.RetrieveUpdateAPIView):
    """
    A class representing an API view for retrieving and updating a FraudString object.

    Attributes:
        permission_classes (tuple): The permission classes required to access this API view.
        queryset (QuerySet): The queryset of FraudString objects to be retrieved and updated.
        serializer_class (Serializer): The serializer class used to serialize and deserialize FraudString objects.
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.FraudString.objects.all()

    serializer_class = serializers.ProfileSerializer


class Search(generics.ListAPIView):
    """
    Search Class

    A class to handle searching for fraud strings.

    Attributes:
        permission_classes (tuple): The permission classes required to access this view.
        queryset: The query set of fraud strings to be searched.
        serializer_class: The serializer class to be used for serializing and deserializing the searched fraud strings.
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.FraudString.objects.all()

    serializer_class = serializers.SearchSerializer
