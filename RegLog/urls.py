from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('profile/', profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_user, name='logout_user'),
]
