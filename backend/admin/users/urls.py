from django.urls import path,include
from .views import register,userDetailsExists,login

urlpatterns = [ 
    path('register', register,name='register') ,
    path('usercheck',userDetailsExists, name='userExists'),
    path('login',login, name='login')
]