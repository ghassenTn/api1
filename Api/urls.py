from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from . import views
urlpatterns = [
    path('',views.FBV_view.as_view()),
    path('add/',views.AddUserView.as_view()),
    path('delete/<int:pk>/',views.DeleteUserView.as_view(),name='delete_user'),
    path('update/<str:name>/',views.UpdateUserView.as_view(),name='update_user_by_name'),
    path('getuserbyname/<str:name>/',views.GetUserByName.as_view(),name='get_user_by_name'),
    path('LoginView/',views.LoginView.as_view(),name='login_user'),
]
