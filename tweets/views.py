from django.shortcuts import render
from .models import Tweet
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

class TweetSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Tweet
        fields = ['id', 'user', 'payload', 'created_at']

class TweetListView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

# 리팩터링한 UserTweetListView
class UserTweetListView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)