from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantFoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantFoodItem
        fields = '__all__'


class RestaurantMenuSerializer(serializers.ModelSerializer):
    food_items = serializers.SerializerMethodField()

    def get_food_items(self, obj):
        if (obj.food_item.count()) > 0:
            splitlist1 = obj.food_item.all()
            user_passion = RestaurantFoodItemSerializer(splitlist1, many=True)
            # user_passion = ",".join([str(i.passion) for i in splitlist1])
            return user_passion.data
        else:
            return "-"

    
    class Meta:
        model = RestaurantMenu
        fields = ('vote','id','food_items','restaurant_id','date','food_item',)
        
        

    def to_representation(self, instance):
            response = super().to_representation(instance)
            # response['food_item'] = RestaurantFoodItemSerializer(instance.food_item).data
            response['restaurant_id'] = RestaurantSerializer(instance.restaurant_id).data 
            return response

class RestaurantMenuVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantMenuVote
        fields = '__all__'


class UserVoteRestaurantMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserVoteRestaurantMenu
        fields = '__all__'

    

    