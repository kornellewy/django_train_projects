from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from .models import Tweet

User = get_user_model()


class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="kjn1", email="kjn1@kjn.pl", password="kjn1")
        self.user2 = User.objects.create_user(username="kjn2", email="kjn2@kjn.pl", password="kjn2")

    def test_tweet_created(self):
        tweet_obj = Tweet.objects.create(content = "dupa", user=self.user)
        self.assertEqual(tweet_obj.user, self.user)
        self.assertEqual(tweet_obj.content, "dupa")

    def get_client(self):
        client = APIClient()
        client.login(username="kjn1", password="kjn1")
        return client
        
    def test_test_list(self):
        client = self.get_client()
        client.login(username="kjn1", password="kjn1")