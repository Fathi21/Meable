from django.db import models

# Create your models here.

from datetime import datetime

from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Profile (models.Model):
    Bio = models.TextField()
    profileImage = models.ImageField(upload_to='images/')
    backroundImage = models.ImageField(upload_to='images/')
    Date = models.DateTimeField(default=datetime.now, blank=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
  

    def __str__(self):
        return str(self.userID) if self.userID else ''
    

    class Meta:
        verbose_name_plural = "Profile"


class posts (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    images = models.ImageField(upload_to='images/')
    tags = TaggableManager()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    DatePosted = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.userID) if self.userID else ' '
        
    class Meta:
        verbose_name_plural = "posts"


class commets (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    postID = models.ForeignKey(posts, on_delete=models.CASCADE)
    comment = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    DateCommented = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.comment
    

    class Meta:
        verbose_name_plural = "commets"

class like (models.Model):
    postID = models.ForeignKey(posts, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    DateLiked = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.userID) if self.userID else ' '

class dislike (models.Model):
    postID = models.ForeignKey(posts, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    DateLiked = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.userID) if self.userID else ' '

class Opinions (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    opinion  = models.TextField()
    tags = TaggableManager()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    DatePosted = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.opinion) if self.opinion else ' '
    
    class Meta:
        verbose_name_plural = "Opinions"

class Agree (models.Model):
    OpinionID = models.ForeignKey(Opinions, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.OpinionID) if self.OpinionID else ' '
    

class Disagree (models.Model):
    OpinionID = models.ForeignKey(Opinions, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.OpinionID) if self.OpinionID else ' '
    


class followers (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    UserFollowed = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.userID ) if self.userID else ''

    class Meta:
        verbose_name_plural = "followers"

class Inbox(models.Model):
    SenderID = models.ForeignKey(User, on_delete=models.CASCADE); # who starts messaging
    ReciverId = models.IntegerField() # second user
    Date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
            return str(self.id) if self.id else ' '

class Messages (models.Model):
    SenderID = models.ForeignKey(User, on_delete=models.CASCADE)
    ReciverID = models.IntegerField()
    Message = models.TextField()
    ReciverReadYet = models.BooleanField(default=False)
    profileID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    inboxID = models.ForeignKey(Inbox, on_delete=models.CASCADE); # message belongs to the inbox
    Date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.Message) if self.Message else ' '
    
    class Meta:
        verbose_name_plural = "Messages"


class eyes (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    userWaslookedID = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "eyes"

    def __str__(self):
        return str(self.userID) if self.userID else ' '

class Videos(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    videoTitle = models.CharField(max_length=500)
    video = models.FileField(upload_to='videos/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.videoTitle


class CommentVideos(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    VideoID = models.ForeignKey(Videos, on_delete=models.CASCADE)
    comment  = models.TextField()
    Date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'Comments for videos'
         
    def __str__(self):
        return str(self.VideoID) if self.VideoID else ' '

class Views (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    VideoID = models.ForeignKey(Videos, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'Views'
         
    def __str__(self):
        return str(self.userID) if self.userID else ' '

class LovedTheVideo (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    VideoID = models.ForeignKey(Videos, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'People loved the video'
         
    def __str__(self):
        return str(self.VideoID) if self.VideoID else ' '

class BugReport (models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    DescribeTheBug = models.TextField()
    AttachScreenshot = models.ImageField(upload_to='images/')
    Date = models.DateTimeField(default=datetime.now, blank=True)


    class Meta:
        verbose_name_plural = 'Bug Reports'
         
    def __str__(self):
        return self.userID





