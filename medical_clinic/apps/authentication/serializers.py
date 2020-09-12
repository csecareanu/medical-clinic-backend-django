from rest_framework import serializers
from medical_clinic.apps.authentication.models.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_no', 'user_type', 'first_name', 'last_name', 'date_of_birth', 'county', 'locality',
                  'email', 'is_active', 'date_joined']


"""
class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_no', 'user_type', 'first_name', 'last_name', 'is_active']
"""
