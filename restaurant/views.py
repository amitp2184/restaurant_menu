from django.shortcuts import render
from .serializers import *
from core.utils import generate_access_token, generate_refresh_token
from rest_framework.views import APIView
# from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import pagination
from rest_framework.filters import SearchFilter
from rest_framework import filters
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from core.models import *

# # Create your views here.

class AddRestaurantView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all() 

    def post(self, request,format='json'):
        
        serilaizer = RestaurantSerializer(data=request.data)
        if serilaizer.is_valid() :
            
            serilaizer.save()
            return Response({
                    "responseCode": 1,
                    "responseMessage": "Add Restaurent Data",
                    "responseData": serilaizer.data
            },status=status.HTTP_200_OK)
        else :
            return Response({
                "responseCode": 0,
                "responseMessage": "No  Data Added",
                "responseData": []
        },status=status.HTTP_200_OK)


class GetRestaurantView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RestaurantSerializer
    # permission_classes = (Check_API_KEY_Auth,)

    def get(self, request):
        getRes = Restaurant.objects.all().order_by('-point') 
        getRes_serializer = RestaurantSerializer(getRes, many=True)
        
        return Response({
                        "responseCode": 1,
                        "responseMessage": "Restaurant Detail",
                        "responseData": 
                                       getRes_serializer.data, 
                                    },
                        status=status.HTTP_200_OK)   
       

class GetRestaurantFoodItemView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RestaurantFoodItemSerializer
    # permission_classes = (Check_API_KEY_Auth,)

    def get(self, request,restaurant_id):
        getRes = RestaurantFoodItem.objects.filter(restaurant_id=restaurant_id) 
        getRes_serializer = RestaurantFoodItemSerializer(getRes, many=True)
        
        return Response({
                        "responseCode": 1,
                        "responseMessage": "Restaurent Food  Detail",
                        "responseData": 
                                       getRes_serializer.data, 
                                    },
                        status=status.HTTP_200_OK) 



class AddRestaurantFoodItemView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantFoodItemSerializer
    queryset = RestaurantFoodItem.objects.all() 

    def post(self, request,format='json'):
        if RestaurantFoodItem.objects.filter(restaurant_id=request.data['restaurant_id'], name= request.data['name']) :
            return Response({
                "responseCode": 0,
                "responseMessage": "data Already Added",
                "responseData": None
        },status=status.HTTP_200_OK)

        serilaizer = RestaurantFoodItemSerializer(data=request.data)
        if serilaizer.is_valid() :
            
            serilaizer.save()
            return Response({
                    "responseCode": 1,
                    "responseMessage": "Add Restaurent Food Item Data",
                    "responseData": serilaizer.data
            },status=status.HTTP_200_OK)
        else :
            return Response({
                "responseCode": 0,
                "responseMessage": "No  Data Added",
                "responseData": []
        },status=status.HTTP_200_OK)


class AddRestaurantMenuView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantMenuSerializer
    queryset = RestaurantMenu.objects.all() 

    def post(self, request,format='json'):
      

        serilaizer = RestaurantMenuSerializer(data=request.data)
        if serilaizer.is_valid() :
            
            serilaizer.save()
            return Response({
                    "responseCode": 1,
                    "responseMessage": "Add Restaurent menu Data",
                    "responseData": serilaizer.data
            },status=status.HTTP_200_OK)
        else :
            return Response({
                "responseCode": 0,
                "responseMessage": "No  Data Added",
                "responseData": []
        },status=status.HTTP_200_OK)


class GetRestaurantMenuByDateView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('date','restaurant_id')

    def get_queryset(self):
        result = RestaurantMenu.objects.filter(date=self.request.GET['date'],restaurant_id=self.request.GET['restaurant_id'])
        
        return result

    def get(self, request, *args, **kwargs):

        response = super(GetRestaurantMenuByDateView, self).get(request, *args, **kwargs)
        return Response({
                "responseCode": 1,
                "responseMessage": "Restaurent Data by Date",
                "responseData": response.data
            })


class AddRestaurantMenuVoteView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserVoteRestaurantMenuSerializer
    queryset = UserVoteRestaurantMenu.objects.all() 

    def post(self, request,format='json'):
        try:
            for i in range(len(request.data['restaurent_menu_id'])):
                user_id = Employee.objects.filter(id=request.data['user_id'] )
                restaurent_id = RestaurantMenu.objects.filter(id=request.data['restaurent_menu_id'][i])
                valnum = UserVoteRestaurantMenu.objects.filter(date=request.data['date'],emp_id =request.data['user_id'] )
                if valnum:
                    return Response({
                            "responseCode": 0,
                            "responseMessage": "User Alread Vote for Three Restaurent Menu",
                            "responseData": None
                    },status=status.HTTP_200_OK)               
                    
                valNew1 = RestaurantMenu.objects.filter(id=request.data['restaurent_menu_id'][i], date=request.data['date'])
                val1= valNew1[0]
                val1.vote = val1.vote +1
                val1.save(update_fields=("vote",))

                UserVoteRestaurantMenu.objects.create(restaurent_menu_id=restaurent_id[0],emp_id =user_id[0],date=request.data['date'] )
            return Response({
                "responseCode": 1,
                "responseMessage": "User Add Vote for Restaurent Menu",
                "responseData": None
        },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"responseCode": 0,
                            "responseMessage": "Data Not Found",
                            "responseData": None},
                        status=status.HTTP_200_OK)

class GetRestaurantMenuVoteByDateView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('date','restaurant_menu_id',)

    def get_queryset(self):
        result = RestaurantMenu.objects.filter(date=self.request.GET['date'],id=int(self.request.GET['restaurant_menu_id']))
        
        return result

    def get(self, request, *args, **kwargs):

        response = super(GetRestaurantMenuVoteByDateView, self).get(request, *args, **kwargs)
        return Response({
                "responseCode": 1,
                "responseMessage": "Restaurent Menu Vote By Date",
                "responseData": response.data
            })
    

class GettingResultView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RestaurantMenuVote.objects.all()
    serializer_class = RestaurantMenuSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('date',)

    def get_queryset(self):
        
        result = RestaurantMenu.objects.filter(date=self.request.GET['date']).order_by('-vote')
        
        return result

    def get(self, request, *args, **kwargs):

        response = super(GettingResultView, self).get(request, *args, **kwargs)
        return Response({
                "responseCode": 1,
                "responseMessage": "Restaurent menu Vote By Date",
                "responseData": response.data
            })

from .models import *
class AddRestaurantMenuVoteViewV2(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserVoteRestaurantMenuSerializer
    queryset = UserVoteRestaurantMenu.objects.all() 

    def post(self, request,format='json'):
        
        try:
            
            for i in range(len(request.data['restaurent_menu_id'])):
                user_id = Employee.objects.filter(id=request.data['user_id'] )
                restaurent_id = RestaurantMenu.objects.filter(id=request.data['restaurent_menu_id'][i])
                valnum = UserVoteRestaurantMenu.objects.filter(date=request.data['date'],emp_id =request.data['user_id'] )
                if len(valnum) > 2:
                    return Response({
                            "responseCode": 1,
                            "responseMessage": "User Alread Vote for Three Restaurent Menu",
                            "responseData": None
                    },status=status.HTTP_200_OK)               
                    
                valNew1 = RestaurantMenu.objects.filter(id=request.data['restaurent_menu_id'][i], date=request.data['date'])
                val1= valNew1[0]
                val1.vote = val1.vote +1
                val1.save(update_fields=("vote",))

                UserVoteRestaurantMenu.objects.create(restaurent_menu_id=restaurent_id[0],emp_id =user_id[0],date=request.data['date'] )
            return Response({
                "responseCode": 1,
                "responseMessage": "User Add Vote for Restaurent Menu",
                "responseData": []
        },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"responseCode": 0,
                            "responseMessage": "Data Not Found",
                            "responseData": None},
                        status=status.HTTP_200_OK)


                