from django.conf import settings

from rest_framework import serializers

from .models import Tweet


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in settings.TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("this is not valid action")
        return value

class TweetCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes']

    def validate_content(self, value):
        if len(value)>settings.MAX_LENGTH:
            raise serializers.ValidationError("This tweet is to long.")
        return value
    
    def get_likes(self, obj):
        return obj.likes.count()
        
class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    # parent = TweetCreateSerializer(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes', 'is_retweet', 'parent']

    def get_likes(self, obj):
        return obj.likes.count()

    def get_content(self, obj):
        content = obj.content
        if obj.is_retweet:
            content = obj.parent.content
        return content
        
    

        