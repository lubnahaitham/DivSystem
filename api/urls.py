from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.authtoken.views import obtain_auth_token  
from knox import views as knox_views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('list/', views.personal_data_list),
    path('detail/<int:pk>/', views.personal_data_detail),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('login/', obtain_auth_token), 
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
