from  rest_framework import serializers
from . import models
from nomadgram.users import models as user_models
from taggit_serializer.serializers import (TagListSerializerField,TaggitSerializer)


class SmallImageSerializer(serializers.ModelSerializer):

    """ Used for the notification"""

    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class CountImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count',
        )


class FeedUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        mdoel = user_models.User
        fields = (
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',   
        )


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__' 

class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'count_likes',
            'creator',
            'tags',
            'created_at',
        )


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Image
        fields=(
            'file',
            'location',
            'caption',
        )

