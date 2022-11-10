from rest_framework import serializers

from home.models import Person


class PersonPortalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('name', 'age', 'address', 
                'phone_number', 'email', 
                'id_company', 'created_at', 'updated_at')