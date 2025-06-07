
from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    #First parameter the url,second the called func, third is the name of
    path('list/', views.post_list , name='post_list'),
    #<> means there is an argument from the user
    path('<int:id>/', views.post_detail, name= 'post_detail'),
   
]
