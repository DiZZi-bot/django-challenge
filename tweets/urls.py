from django.urls import path
from . import views

urlpatterns = [
    path('tweets/', views.TweetList.as_view(), name='tweet-list'),
    path('tweets/<int:pk>/', views.TweetDetail.as_view(), name='tweet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/tweets/', views.UserTweets.as_view(), name='user-tweets'),
    path('users/password/', views.ChangePassword.as_view(), name='change-password'),
]
