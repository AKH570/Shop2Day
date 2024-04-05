from django.urls import path
from Accounts import views
urlpatterns=[
    path('registrationform/',views.UserRegistraionform,name='registrationform'),
    path('login/',views.UserLogin,name='login'),
    path('logout/',views.UserLogout,name='logout'),
]