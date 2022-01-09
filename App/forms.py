from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class CreatePostFrom(ModelForm):
    class Meta:
        model = posts
        fields = "__all__"
        exclude = ["userID", "DatePosted", "profile"]

        labels = {      
            "post": "What's happening?",
            "Tags": "What's happening?",     
        }


class CreateProfileFrom(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        
        exclude = ["Date", "userID"]

        labels = {      
            "profileImage": "Profile Picture",
            "backroundImage": "Add Cover Photo",     
        }

class CreateOpinionsFrom(ModelForm):
    class Meta:
        model = Opinions
        fields = "__all__"

        exclude = ["DatePosted", "userID", "profile"]



class CreateCommetsFrom(ModelForm):
    class Meta:
        model = commets
        fields = "__all__"

        exclude = ["userID", "postID", "profile", "DateCommented"]


class CreateVideoFrom(ModelForm):
    class Meta:
        model = Videos
        fields = "__all__"

        exclude = ["userID", "profile", "Date"]

        labels = {      
            "videoTitle": "Description",   
        }


class CreateCommentVideosFrom(ModelForm):
    class Meta:
        model = CommentVideos
        fields = "__all__"


        exclude = ["userID", "VideoID", "VideoID", "Date"]

       

class MessagesFrom(ModelForm):
    class Meta:
        model = Messages
        fields = "__all__"

        exclude = ["SenderID", "ReciverID", "ReciverReadYet", "profileID", "inboxID", "Date"]


class followersFrom(ModelForm):
    class Meta:
        model = followers
        fields = "__all__"

        exclude = ["userID", "UserFollowed", "profile", "Date"]
