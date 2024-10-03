from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('api/v1/tweets/', views.TweetListView.as_view(), name='tweet_list'),
    path('api/v1/users/<int:user_id>/tweets/', views.UserTweetListView.as_view(), name='user_tweet_list'),
]