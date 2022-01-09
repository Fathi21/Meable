from rest_framework import serializers
from .models import *

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = like
        fields ='__all__'


class dislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = dislike
        fields ='__all__'


class AgreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agree
        fields ='__all__'


class DisagreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disagree
        fields ='__all__'


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = followers
        fields ='__all__'


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = commets
        fields ='__all__'


class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        exclude = ["password", "last_login", "is_superuser", "username", "email", "is_staff", "is_active", "groups", "user_permissions"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =["id", "profileImage", "userID"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = '__all__'


class eyesSerializer(serializers.ModelSerializer):
    class Meta:
        model = eyes
        fields = '__all__'


class CommentVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentVideos
        fields = '__all__'



class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views
        fields = '__all__'


class LovedTheVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LovedTheVideo
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'


class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = '__all__'