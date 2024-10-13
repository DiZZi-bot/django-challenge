from rest_framework import serializers
from .models import Tweet, Like
from django.contrib.auth.models import User

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'payload', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'tweet', 'created_at']
