from django.urls import path
from .views import LoginView, RegisterUsersView

urlpatterns = [
    # path('current_user/', current_user),
    # path('users/', UserList.as_view()),
    path('user/login/',
         LoginView.as_view(), name="auth-login"),
    path('user/signup/', RegisterUsersView.as_view(), name="user-signup"),


]
