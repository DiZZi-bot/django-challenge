from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Tweet, Like
from .serializers import TweetSerializer, UserSerializer, LikeSerializer

# 트윗 목록, 생성
class TweetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 트윗 조회, 수정, 삭제
class TweetDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            tweet = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = Tweet.objects.get(pk=pk)
        if tweet.user != request.user:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        serializer = TweetSerializer(tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tweet = Tweet.objects.get(pk=pk)
        if tweet.user != request.user:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 사용자 목록, 생성
class UserList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 사용자 조회
class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

# 사용자의 트윗 조회
class UserTweets(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

# 비밀번호 변경
class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        password = request.data.get('password')
        if password:
            user.set_password(password)
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Password not provided"}, status=status.HTTP_400_BAD_REQUEST)
