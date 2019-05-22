from django.urls import path ,include
from user_auth_app import views

app_name = "user_auth_app"

urlpatterns = [
    path(r'user',views.user_auth_index,name = "user_index"),
    path(r'user/login/',views.user_login,name = "user_login"),
    path(r'user/register/',views.registration,name = "user_registration"),
    path(r'user/logout/',views.user_logout,name="user_logout"),
    path(r'user/special/',views.special,name="user_special"),

]