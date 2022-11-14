from django.urls import path ,re_path
from . import views

urlpatterns = [
   
    path('addRestaurant/', views.AddRestaurantView.as_view(),name = 'add_restaurant' ),
    path('getRestaurant/', views.GetRestaurantView.as_view(),name = 'get_restaurant' ),
    re_path(r'getRestaurantFoodItem/(?P<restaurant_id>[0-9a-f-]+)/$', views.GetRestaurantFoodItemView.as_view(),name = 'get_restaurant_food_item' ),
     path('addRestaurantFoodItem/', views.AddRestaurantFoodItemView.as_view(),name = 'add_restaurant_food_item' ),
     path('addRestaurantMenu/', views.AddRestaurantMenuView.as_view(),name = 'add_restaurant_menu' ),
    path('getRestaurantMenu/', views.GetRestaurantMenuByDateView.as_view(),name = 'get_restaurant_menu' ),
     
    path('addRestaurantMenuVote/', views.AddRestaurantMenuVoteView.as_view(),name = 'add_restaurant_menu_vote' ),
    # path('getRestaurantMenuVote/', views.GetRestaurantMenuVoteByDateView.as_view(),name = 'get_restaurant_menu_vote' ),
    path('addRestaurantMenuVote/V2/', views.AddRestaurantMenuVoteViewV2.as_view(),name = 'add_restaurant_menu_vote_v2' ),
    path('gettingResult/', views.GettingResultView.as_view(),name = 'get_result' ),

]