from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from system.models import Customer
from system.serializers import CustomerSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def customer_list(request):
    # GET list of customers, POST a new customer, DELETE all customers
    if request.method == 'GET':
        customers = Customer.objects.all()
        
        email = request.GET.get('email', None)
        if email is not None:
            customers = customers.filter(email__icontains=email)
        
        customer_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Customer.objects.all().delete()
        return JsonResponse({'message': '{} Customers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    # find customer by pk (id)
    try: 
        customer = Customer.objects.get(pk=pk) 
    except Customer.DoesNotExist: 
        return JsonResponse({'message': 'The customer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE customer
    # ... customer = Customer.objects.get(pk=pk)
 
    if request.method == 'GET': 
        customer_serializer = CustomerSerializer(customer) 
        return JsonResponse(customer_serializer.data) 
    elif request.method == 'PUT': 
        customer_data = JSONParser().parse(request) 
        customer_serializer = CustomerSerializer(customer, data=customer_data) 
        if customer_serializer.is_valid(): 
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        customer.delete() 
        return JsonResponse({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
