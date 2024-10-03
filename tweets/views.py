from django.shortcuts import render
from .models import Tweet
from django.contrib.auth.models import User
from rest_framework import serializers
from django.views import View
from django.http import JsonResponse

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.CharField(source='user.username')
    payload = serializers.CharField()
    created_at = serializers.DateTimeField()

class TweetListView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return JsonResponse(serializer.data, safe=False)

class UserTweetListView(View):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)

        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return JsonResponse(serializer.data, safe=False)