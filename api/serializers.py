from rest_framework import serializers
from .models import PersonalData
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = ('phone_number', 'password')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

    #     return user
    
        
class PersonalSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PersonalData
        fields = '__all__'
        extra_kwargs = {'phone_number': {'required': True},
                        'birthdate': {'required': True},
                        'password': {'write_only': True},
                        }
      
    def validate(self, value):
        if value['phone_number'] < 15:
            raise serializers.ValidationError("Please enter a correct phone number")
        if value['password'] == ['password2']:
            raise serializers.ValidationError("Didn't match")
        if value['birthdate'] != 'YYYY-MM-DD':
            raise serializers.ValidationError("Must be in format 'YYYY-MM-DD', in the past ")
        if value['avatar'] != 'jpg, jpeg, png':
            raise serializers.ValidationError("Supported content types 'jpg, jpeg, png' ")
        return value
        
 