from .models import Volunteer_User
from rest_framework import serializers

class Volunteer_UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Volunteer_User
        fields = '__all__'
