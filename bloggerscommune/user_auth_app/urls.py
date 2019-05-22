from django.urls import path ,include
from user_auth_app import views

app_name = "user_auth_app"

urlpatterns = [
    path(r'',views.user_auth_index,name = "user_index"),
    path(r'login/',views.user_login,name = "user_login"),
    path(r'register/',views.registration,name = "user_registration"),
    path(r'logout/',views.user_logout,name="user_logout"),

]