from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import User
from .models_choices import UserTypeChoice
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # populate the 'request' object with user data
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAdminUser]

    serializer_class = UserSerializer
    queryset = User.objects.none()


"""
    @action(detail=False)
    def patients(self, request, pk=None):
        users = User.objects.filter(user_type=UserTypeChoice.PATIENT)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def doctors(self, request, pk=None):
        users = User.objects.filter(user_type=UserTypeChoice.DOCTOR)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def secretaries(self, request, pk=None):
        users = User.objects.filter(user_type=UserTypeChoice.SECRETARY)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def details(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)
"""
