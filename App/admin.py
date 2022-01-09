from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(posts)
admin.site.register(commets)
admin.site.register(like)
admin.site.register(dislike)
admin.site.register(Agree)
admin.site.register(Disagree)
admin.site.register(followers)
admin.site.register(Messages)
admin.site.register(Profile)
admin.site.register(Opinions)
admin.site.register(eyes)
admin.site.register(Videos)
admin.site.register(CommentVideos)
admin.site.register(LovedTheVideo)
admin.site.register(Views)
admin.site.register(BugReport)
admin.site.register(Inbox)
