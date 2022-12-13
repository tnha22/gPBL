from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps.api.models import User, Shift, Camera, Log, Face


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','password', 'username', 'email', 'age', 'address', 
                'phone_number', 'id_company','image')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, 
        validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password', 'password2',
                  'age', 'address', 'phone_number', 'id_company','image')
        extra_kwargs = {
            'name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            age=validated_data['age'],
            address=validated_data['address'],
            phone_number=validated_data['phone_number'],
            id_company=validated_data['id_company'],
            image = validated_data['image'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
class ShiftSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['end_time'] < attrs['start_time']:
            raise serializers.ValidationError(
                {"end_time": "end_time smaller than start_time"})
        return attrs
    class Meta:
        model = Shift
        fields = ('id', 'name', 'start_time', 'end_time', 'date', 'user')
    
class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = ('id','name','feature', 'user')

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('id','name','url')
    
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id','time_in','user','camera')

        
