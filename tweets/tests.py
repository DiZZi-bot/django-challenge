from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Tweet

class APITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_get_tweets(self):
        url = reverse('tweet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tweet(self):
        url = reverse('tweet-list')
        data = {'payload': 'This is a test tweet'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_tweet(self):
        tweet = Tweet.objects.create(user=self.user, payload='Old Content')
        url = reverse('tweet-detail', args=[tweet.pk])
        data = {'payload': 'Updated Content'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_tweet(self):
        tweet = Tweet.objects.create(user=self.user, payload='Content to delete')
        url = reverse('tweet-detail', args=[tweet.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
