from rest_framework import serializers
from .models import *


class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = '__all__'
        