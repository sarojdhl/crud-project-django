from userapp.models import User
from rest_framework import serializers

# Create your tests here.
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
