from django.urls import path, include
from .views import *
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', ActivateView.as_view()),
    path('login/', LogInView.as_view()),
    path('logout/', LogOutView.as_view()),
]