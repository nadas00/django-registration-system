from rest_framework import serializers 
from system.models import Customer
 
 
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields =  ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'id_number',
                  'phone_number',
                  'password')