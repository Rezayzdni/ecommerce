from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),

    path('music-detail/',views.music_detail,name='music_detail'),

    path('music-detail-detail/',views.music_detail_detail,name='music_detail_detail'),
    
    path('music-detail-detail/solve-exercise/',views.solve_exercise,name='solve_exercise'),
    
    path('customer-profile/',views.customer_profile,name='customer_profile'),
    
    path('my-saved-products/',views.my_saved_products,name='my_saved_products'),
    
    path('customer-profile-detail/',views.custom_profile_detail,name='customer_profile_detail'),
    
    path('customer-profile-settings/',views.custom_profile_settings,name='customer_profile_settings'),

]