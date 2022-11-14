from django.db import models
from core.models import *
# Create your models here.
class Restaurant(models.Model):
    
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null = True , blank=True) 
    point = models.IntegerField(null= True,blank=True)
    remark = models.CharField(max_length=255, null = True , blank=True )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) :
        return str(self.id)

    class Meta:
        db_table = "restaurant"
    

class RestaurantFoodItem(models.Model):
    
    id  = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255, null = True , blank=True) 
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE ,related_name="restaurant_food_item" )
    remark = models.CharField(max_length=255, null = True , blank=True )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) :
        return str(self.id)

    class Meta:
        db_table = "restaurant_food_item"


class RestaurantMenu(models.Model):
    
    id  = models.AutoField(primary_key=True)
    food_item = models.ManyToManyField(RestaurantFoodItem,null=True, blank=True ) 
    food_id = models.ForeignKey(RestaurantFoodItem,on_delete=models.CASCADE ,related_name="restaurant_food",null=True, blank=True ) 
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE ,related_name="restaurant_menu",null=True, blank=True )
    date  = models.DateField(null = True,blank=True)
    remark = models.CharField(max_length=255,  null = True ,blank=True )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    vote = models.IntegerField(default=0)

    def __str__(self) :
        return str(self.id)

    class Meta:
        db_table = "restaurant_menu"



from employee.models import *
class UserVoteRestaurantMenu(models.Model):
    
    id  = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE ,related_name="emp_vote_restaurant",null=True, blank=True )
    user_id = models.ForeignKey(UserAccount,on_delete=models.CASCADE ,related_name="user_Account_restaurant",null=True, blank=True )
    restaurent_menu_id = models.ForeignKey(RestaurantMenu,on_delete=models.CASCADE ,related_name="restaurant_menu_user",null=True, blank=True )
    date  = models.DateTimeField(null = True,blank=True)

    remark = models.CharField(max_length=255,  null = True ,blank=True )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) :
        return str(self.id)

    class Meta:
        db_table = "user_vote_res_menu"


class RestaurantMenuVote(models.Model):
    
    id  = models.AutoField(primary_key=True)

   
    restaurant_menu_id = models.ForeignKey(RestaurantMenu,on_delete=models.CASCADE ,related_name="restaurant_menu_vote",null=True, blank=True )
    vote = models.IntegerField(default=0)
    date  = models.DateField(null = True,blank=True)
    remark = models.CharField(max_length=255,  null = True ,blank=True )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) :
        return str(self.id)

    class Meta:
        db_table = "restaurant_menu_vote"
