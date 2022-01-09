from django.shortcuts import HttpResponse, render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.contrib import messages
from .models import *
from .forms import *
from rest_framework import status


## rest_framework API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from taggit.models import Tag
from django.db.models import Q, Avg, Max, Count


@login_required(login_url='signIn')
def home(request):

    ProfileTable = Profile.objects.filter(userID = request.user.id).count()
    OpinionsTable = Opinions.objects.order_by("?")[:5]
    userTable = Profile.objects.order_by("?")[:5]
    VideosTable = Videos.objects.order_by("?")[:5]


    if (ProfileTable > 0):

        profileImg = Profile.objects.get(userID = request.user.id)

        getProfileID = Profile.objects.get(userID = request.user.id)

        fromPost = CreatePostFrom()
            
        if request.method == "POST":
            fromPost = CreatePostFrom(request.POST, request.FILES)

            if fromPost.is_valid():
                fromPost.instance.userID = request.user
                fromPost.instance.profile = getProfileID
                fromPost.save()
                return redirect("home")

            else:
                pass
        
        user = request.user
        followed_people = followers.objects.filter(userID = request.user).values('UserFollowed')
        allPosts = posts.objects.filter(Q(userID__in=followed_people) | Q(userID=request.user)).order_by('-DatePosted')
            
        context = {
            "fromPost" : fromPost,
            "allPosts" : allPosts,
            "profileImg" :profileImg,
            "OpinionsTable" : OpinionsTable,
            "userTable" : userTable,
            "VideosTable" : VideosTable
        }
        return render (request, 'Pages/home.html', context) 

    else:
        return redirect("profile", request.user.id)


@login_required(login_url='signIn')
def opinions(request):
    ProfileTable = Profile.objects.filter(userID = request.user.id).count()

    if (ProfileTable > 0):

        RandomOpinions = Opinions.objects.order_by("?")[:10]
       
        profileImg = Profile.objects.get(userID = request.user.id)

        getProfileID = Profile.objects.get(userID = request.user.id)

        opinionForm = CreateOpinionsFrom()

        followed_people = followers.objects.filter(userID = request.user).values('UserFollowed')
        allOpinions = Opinions.objects.filter(Q(userID__in=followed_people) | Q(userID=request.user)).order_by('-DatePosted')

        if request.method == "POST":
            opinionForm = CreateOpinionsFrom(request.POST)
            if opinionForm.is_valid():
                opinionForm.instance.userID = request.user
                opinionForm.instance.profile = getProfileID
                opinionForm.save()
                return redirect("opinions")

        

        context = {
            "profileImg":profileImg,
            "opinionForm" : opinionForm,
            "allOpinions" : allOpinions,
            "RandomOpinions" : RandomOpinions
        }

        return render(request, "Pages/opinions.html", context)

    else:
        return redirect("profile", request.user.id)
   

@login_required(login_url='signIn')
def opinionDetail(request, pk):

    OpinionExit = Opinions.objects.filter(id = pk).count()
    if(OpinionExit > 0):
        allOpinions = Opinions.objects.filter(id = pk)
        profileImg = Profile.objects.get(userID = request.user.id)

        OpinionTableEdit = Opinions.objects.get(id = pk)

        getAllOpinionsFromUser = Opinions.objects.filter(userID = OpinionTableEdit.userID)

        EditOpinion = CreateOpinionsFrom(instance = OpinionTableEdit)

        if request.method == 'POST':
            
            EditOpinion = CreateOpinionsFrom(request.POST, request.FILES, instance = OpinionTableEdit) 

            if EditOpinion.is_valid():
                print("SAVING")
                EditOpinion.save()

        context = {
            "allOpinions":allOpinions,
            "profileImg" : profileImg,
            "EditOpinion" : EditOpinion,
            "getAllOpinionsFromUser" : getAllOpinionsFromUser
        }

        return render(request, "Pages/opinionDetail.html", context)
    else:
        return redirect("home")


@login_required(login_url='signIn')
def tag_ForOpinions(request, tag):

    OpinionsTable = Opinions.objects.filter(tags__name__in=[tag])
    profileImg = Profile.objects.get(userID = request.user.id)

    context = {
        "OpinionsTable"  : OpinionsTable,
        "tag":tag,
        "profileImg" : profileImg
    }

    return render (request, 'Pages/tag_forOpinions.html', context)


@login_required(login_url='signIn')
def profile(request, pk):

    checkUserInDatabase = User.objects.filter(id = pk).count()
    
    userLoggedIn = str(request.user.id)
    userIDFromURl = str(pk)
    checkProfileInDatabase = Profile.objects.filter(userID = pk).count()
    
    if (checkProfileInDatabase == 0):
        ProfilID_forEyesTable = ""
    else:
        ProfilID_forEyesTable = Profile.objects.get(userID = request.user.id)

    if (checkUserInDatabase > 0):
        userProfileDetails = User.objects.get(id = pk)
        profileForm = CreateProfileFrom()

        if request.method == "POST" and 'CreateProfile' in request.POST:
            profileForm = CreateProfileFrom(request.POST, request.FILES)
            if profileForm.is_valid():
                profileForm.instance.userID = request.user
                profileForm.save()
                print(">>>>>>>>>>>>>>>")
                print("USER CREATE PROFILE")
                print(">>>>>>>>>>>>>>>") 
                return redirect("home")

        followingForm = followersFrom()

        urlID = pk

        userID = request.user.id

        profileTable = Profile.objects.get(userID = urlID)

        profileID = profileTable.id

        userCurrentUserFollowed = User.objects.get(id = request.user.id)

        print("USERID:", userCurrentUserFollowed)

        allPosts = posts.objects.filter(userID=pk)

        allOpinions = Opinions.objects.filter(userID=pk)

        allVideos = Videos.objects.filter(userID=pk)

        userFollowedAlready = followers.objects.filter(Q(userID=request.user) | Q(UserFollowed=pk)).count()

        if (userFollowedAlready == 0):
            if request.method=='POST' and 'followUser' in request.POST:
                followingForm = followersFrom(request.POST, request.FILES)
                if followingForm.is_valid():
        
                    followingForm.instance.userID = request.user
                    followingForm.instance.UserFollowed = pk
                    followingForm.instance.profile = profileTable
                    followingForm.save()
                    return redirect("profile", pk)

                    print(">>>>>>>>>>>>>>>")
                    print("FOLLOWING")
                    print(">>>>>>>>>>>>>>>") 

                else:
                    print("NOT FOLLLOWED")
        else:
            print("YOU FOLLOWED THIS USER ALREADY")


        if request.method=='POST' and 'UnfollowUser' in request.POST:
            deleteThisUser = followers.objects.filter(Q(userID=request.user) | Q(UserFollowed=userCurrentUserFollowed.id)).delete()
            return redirect("profile", pk)

            print("UnfollowUser")
    
            
                         

        userTable = User.objects.get(id = pk)
        
        first_nameAndlast_name = userTable.first_name + " " + userTable.last_name  

        if (checkProfileInDatabase > 0):
            profileTable = Profile.objects.get(userID = pk)

            EditProfile = CreateProfileFrom(instance = profileTable)

            if request.user == profileTable.userID:
                if request.method == 'POST' and 'EditProfile' in request.POST:
                    EditProfile = CreateProfileFrom(request.POST, request.FILES, instance = profileTable) 

                    if EditProfile.is_valid():
                        print(">>>>>>>>>>>>>>>")
                        print("Editing profile")
                        print(">>>>>>>>>>>>>>>")

                        EditProfile.save()

                        return redirect("profile", request.user.id)


                    else:
                        print("YOU CAN NOT EDIT")

            context = {
                "first_nameAndlast_name":first_nameAndlast_name,
                "checkUserInDatabase" : checkUserInDatabase,
                "checkProfileInDatabase" : checkProfileInDatabase,
                "profileTable" :profileTable,
                "pk" : pk,
                "userLoggedIn" : userLoggedIn,
                "EditProfile" : EditProfile,
                "userProfileDetails" : userProfileDetails,
                "userIDFromURl" : userIDFromURl,
                "ProfilID_forEyesTable" : ProfilID_forEyesTable,
                "followingForm" : followingForm,
                "userFollowedAlready" : userFollowedAlready,
                "allPosts" : allPosts,
                "allOpinions" : allOpinions,
                "allVideos" : allVideos
 
            }

        else:
            context = {
                "first_nameAndlast_name":first_nameAndlast_name,
                "checkUserInDatabase" : checkUserInDatabase,
                "checkProfileInDatabase" : checkProfileInDatabase,
                "profileForm" : profileForm,
                "userProfileDetails" : userProfileDetails,
                "userIDFromURl" : userIDFromURl,
                "ProfilID_forEyesTable" : ProfilID_forEyesTable,
                "allPosts" : allPosts,
                "allOpinions" : allOpinions,
                "allVideos" : allVideos



                

            }

        #return redirect("eyes", pk)
               
        return render (request, 'Pages/profile.html', context) 

    else:
        context = {
            "checkUserInDatabase":checkUserInDatabase,

        }

        return render (request, 'Pages/profile.html', context) 


@login_required(login_url='signIn')
def tag_detail(request, tag):

    postTable = posts.objects.filter(tags__name__in=[tag])

    context = {
        "postTable":postTable,
        "tag":tag,
    }

    return render (request, 'Pages/tag_detail.html', context) 


@login_required(login_url='signIn')
@api_view(['GET'])
def LikesForAllPost(request, pk):

    Likes = like.objects.filter(postID = pk)

    serializer = LikeSerializer(Likes, many=True)
    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def likeButton(request, pk):
    
    postID = pk

    userID = request.user.id

    postTable = posts.objects.get(id = postID)

    checkIfUserLikedAllReady = like.objects.filter(postID = postID, userID = userID).count()
  
    if checkIfUserLikedAllReady == 0:
        if request.method == 'POST':
            serializer = LikeSerializer(data={'postID': pk, 'userID': userID})

            if serializer.is_valid():
                serializer.save()
                dislike.objects.filter(postID = postID, userID = userID).delete()            
            else:
                pass
            return Response(serializer.data)
    
    else:
        print("USER ALLREADY LIKED")

        return redirect("home")


@login_required(login_url='signIn')
@api_view(['GET'])
def dislikeForAllPost(request, pk):

    dislikes = dislike.objects.filter(postID = pk)

    serializer = LikeSerializer(dislikes, many=True)
    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def dislikeButton(request, pk):
    
    postID = pk

    userID = request.user.id

    postTable = posts.objects.get(id = postID)

    checkIfUserDislikeAllReady = dislike.objects.filter(postID = postID, userID = userID).count()

    print("COUNT DISLIKES: ", checkIfUserDislikeAllReady)
    print("POST ID:", postID)

    if checkIfUserDislikeAllReady == 0:
        if request.method == 'POST':
            serializer = dislikeSerializer(data={'postID': pk, 'userID': userID})

            if serializer.is_valid():
                serializer.save()
                like.objects.filter(postID = postID, userID = userID).delete()
                print("SAVING LIKE")
            
            else:
                print("NOT SAVING LIKE")

            return Response(serializer.data)
    
    else:
        print("USER ALLREADY LIKED")

        return redirect("home")


@login_required(login_url='signIn')
@api_view(['GET'])
def AgreeForAllOpinions(request, pk):

    Agrees = Agree.objects.filter(OpinionID_id = pk)

    serializer = AgreeSerializer(Agrees, many=True)

    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def AgreeButton(request, pk):

    OpinionID = pk

    userID = request.user.id

    Agrees = Agree.objects.filter(OpinionID = OpinionID)

    checkIfUserAgreeAllReady = Agree.objects.filter(OpinionID = OpinionID, userID = userID).count()

    print("COUNT AGREES: ", checkIfUserAgreeAllReady)
    print("Opinion ID:", OpinionID)

    print("AGREE: ", Agrees)

    if checkIfUserAgreeAllReady == 0:
        print ("USER IS ALLOWED TO AGREE")

        if request.method == 'POST':
            serializer = AgreeSerializer(data={'OpinionID': pk, 'userID': userID})

            if serializer.is_valid():
                serializer.save()
                Disagree.objects.filter(OpinionID_id = OpinionID, userID = userID).delete()
                
                print("SAVING AGREE")

            else:
                print("NOT SAVING AGREE")

                print(serializer.is_valid())

            return Response(serializer.data)

    else:
        print("USER ALL READY AGREED")

        return redirect("home")


@login_required(login_url='signIn')
@api_view(['GET'])
def DisagreeForAllOpinions(request, pk):

    Disagrees = Disagree.objects.filter(OpinionID_id = pk)

    serializer = DisagreeSerializer(Disagrees, many=True)

    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def DisagreeButton(request, pk):

    OpinionID = pk

    userID = request.user.id

    Disagrees = Disagree.objects.filter(OpinionID = OpinionID)

    checkIfUserDisagreesAllReady = Disagree.objects.filter(OpinionID = OpinionID, userID = userID).count()

    if checkIfUserDisagreesAllReady == 0:
        print ("USER IS ALLOWED TO DISAGREE")

        if request.method == 'POST':
            serializer = DisagreeSerializer(data={'OpinionID': pk, 'userID': userID})

            if serializer.is_valid():
                serializer.save()
                Agree.objects.filter(OpinionID_id = OpinionID, userID = userID).delete()

                print("SAVING AGREE")
            else:
                print("NOT SAVING AGREE")

                print(serializer.is_valid())

            return Response(serializer.data)

    else:   
        print("USER ALL READY AGREED")

        return redirect("home")


@login_required(login_url='signIn')
@api_view(['GET'])
def followersForEachUser(request, pk):

    followersTable = followers.objects.filter(userID = pk)

    serializer = FollowersSerializer(followersTable, many=True)

    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['GET'])
def followingForEachUser(request, pk):

    followersTable = followers.objects.filter(UserFollowed = pk)

    serializer = FollowersSerializer(followersTable, many=True)

    return Response(serializer.data)
    
    
@login_required(login_url='signIn')
@api_view(['POST'])
def FollowerButton(request, pk):
    
    countFollowers = followers.objects.filter(UserFollowed = pk, userID = request.user.id).count()
    print(">>>>>>>>>>>>>>>>>>")
    print("COUNT FOLLOWER: ", countFollowers)
    print(">>>>>>>>>>>>>>>>>>")

    if countFollowers == 0:

        urlID = pk

        userID = request.user.id

        profileTable = Profile.objects.get(userID = urlID)

        profileID = profileTable.id

        
        print("userID: ", userID)
        print("urlID: ", urlID)
        print("profileID: ", profileID)

        if request.method == 'POST':
            serializer = FollowersSerializer(data={'userID': userID, 'UserFollowed': urlID, 'profile': profileID})

            if serializer.is_valid():
                serializer.save()

                print("SAVING")
            else:
                print("NOT VALID")

                print(serializer.is_valid())

        return Response(serializer.data)
    else:
        return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['GET'])
def CommentsForAllPost(request, pk):

    allCommets = commets.objects.filter(postID = pk).order_by('-id')

    serializer = CommentsSerializer(allCommets, many=True)
    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def CreateComments(request, pk):
    
    if request.method == 'POST':
        serializer = CommentsSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            print("SAVING")
        else:
            print("NOT VALID")

            print(serializer.is_valid())

        return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['GET'])
def AllUsers(request):
    
    allUsers = User.objects.filter(is_superuser = False)

    serializer = usersSerializer(allUsers, many=True)
    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['GET'])
def AllProfile(request):
    
    allProfile = Profile.objects.all()

    serializer = ProfileSerializer(allProfile, many=True)
    return Response(serializer.data)


def signIn(request):

    print(request.user.is_authenticated)

    if request.user.is_authenticated:

        return redirect("home")

    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
                
            else:
                return redirect("signUp")

        return render (request, 'Pages/signIn.html') 
    

def signUp(request):

    #messages.success(request, 'Account was created for ')
    if request.user.is_authenticated:
    
        return redirect("home")

    else:
        fromReg = CreateUserFrom()

        if request.method == "POST":
            fromReg = CreateUserFrom(request.POST)

            if fromReg.is_valid():
                fromReg.save()
                first_name = fromReg.cleaned_data.get("first_name")
                last_name = fromReg.cleaned_data.get("last_name")
                return redirect("signIn")
                

        context = {
            "fromReg" : fromReg,
        }
        return render (request, 'Pages/signUp.html', context)


def logout_view(request):
    logout(request)
    return redirect("signIn")


def PostDetail(request, pk):

    postExist = posts.objects.filter(id = pk).count()

    if(postExist > 0):
    
        profileImg = Profile.objects.get(userID = request.user.id)

        postTable = posts.objects.filter(id = pk)

        commentForm = CreateCommetsFrom()

        profileID = Profile.objects.get(userID = request.user.id)

        countLikes = like.objects.filter(postID = pk).count()

        postTableEdit = posts.objects.get(id = pk)

        userTable = User.objects.get(username = postTableEdit.userID)

        postID = postTableEdit.id

        EditPost = CreatePostFrom(instance = postTableEdit)

        getUserID = posts.objects.get(id = pk)

        getRelatedPosts = posts.objects.filter(userID = getUserID.userID)


        if request.method == 'POST':
            
            EditPost = CreatePostFrom(request.POST, request.FILES, instance = postTableEdit) 

            if EditPost.is_valid():
                print("SAVING")
                EditPost.save()

        context = {
            "profileImg" : profileImg,
            "postTable" : postTable,
            "commentForm" : commentForm,
            "postID" : postID,
            "profileID" : profileID,
            "userTable" : userTable,
            "EditPost" : EditPost,
            "postID" : postID,
            "getRelatedPosts" : getRelatedPosts

        }

        return render (request, 'Pages/postDetail.html', context)
    else:
        return redirect("home")


def deletePost (request, pk):
    delteThisPost = posts.objects.get(id = pk)
    delteThisPost.delete()
    return redirect("home")

@login_required(login_url='signIn')
def commentDetail(request, pk):
    countComment= commets.objects.filter(id = pk).count()

    if countComment == 1:
        comment = commets.objects.get(id = pk)
        profileImg = Profile.objects.get(userID = request.user.id)

        profileCommenter = Profile.objects.get(userID = comment.userID)

        userName = User.objects.get(id = comment.userID.id)
        
        commetsTable = commets.objects.get(id = pk)

        editComments = CreateCommetsFrom(instance = commetsTable)

        userTable = User.objects.get(username = commetsTable.userID)

        if request.method == 'POST':
            
            editComments = CreateCommetsFrom(request.POST, request.FILES, instance = commetsTable) 

            if editComments.is_valid():

                print("SAVING")
                
                editComments.save()

                return redirect("commentForPost", pk)

        context = {
            "comment" : comment,
            "profileCommenter" :profileCommenter,
            "profileImg" : profileImg,
            "userName" : userName,
            "editComments" : editComments
        }

        return render (request, 'Pages/commentDetail.html', context)


    else:

        profileImg = Profile.objects.get(userID = request.user.id)

        context = {
            "countComment" : countComment,
            "profileImg" :profileImg,

        }

        return render (request, 'Pages/commentDetail.html', context)


@login_required(login_url='signIn')
def deleteComment (request, pk):
    delteThisComment = commets.objects.get(id = pk)
    delteThisComment.delete()
    return redirect("home")


@login_required(login_url='signIn')
def deleteOpinions (request, pk):
    delteThisOpinion = Opinions.objects.get(id = pk)
    delteThisOpinion.delete()
    return redirect("home")


@login_required(login_url='signIn')
@api_view(['GET'])
def eyesForEachUser(request, pk):
    eyesForUsers = eyes.objects.filter(userWaslookedID = pk)

    serializer = eyesSerializer(eyesForUsers, many=True)
    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def CreateEyes(request, pk):
    
    ProfilID_forEyesTable = Profile.objects.get(userID = request.user.id)

    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print ("profile id: ", ProfilID_forEyesTable.id)

    if request.method == 'POST':

        serializer = eyesSerializer(data = {'userID': request.user.id, 'userWaslookedID': pk, 'profile': ProfilID_forEyesTable.id})

        if serializer.is_valid():
            serializer.save()

            print("SAVING")
        else:
            print("NOT VALID")
            print("FORM ERRORS: ", serializer.errors)
            print(serializer.is_valid())

        return Response(serializer.data)
    
@login_required(login_url='signIn')
def media(request):

    CreateVideo = CreateVideoFrom()

    profileImg = Profile.objects.get(userID = request.user.id)

    otherVid = Videos.objects.order_by("?")[:5]

    getProfileID = Profile.objects.get(userID = request.user.id)

    VideosTable = Videos.objects.all().order_by('-Date')

    if request.method == 'POST':
        CreateVideo = CreateVideoFrom(request.POST, request.FILES)

        if CreateVideo.is_valid():
            CreateVideo.instance.userID = request.user
            CreateVideo.instance.profile = getProfileID
            CreateVideo.save()
            return redirect("media")

    context = { 
        "CreateVideo" : CreateVideo,
        "profileImg" : profileImg,
        "VideosTable" : VideosTable,
        "otherVid" :otherVid

    }

    return render (request, 'Pages/media.html', context)

@login_required(login_url='signIn')
def deleteVideo(request, pk):
    deleteVideo = Videos.objects.get(id = pk)
    deleteVideo.delete()
    return redirect("home")

@login_required(login_url='signIn')
def mediaDetail(request, pk):

    VideosExist = Videos.objects.filter(id = pk).count()

    if(VideosExist > 0):
        profileImg = Profile.objects.get(userID = request.user.id)

        VideosTable = Videos.objects.filter(id = pk)

        otherVid = Videos.objects.order_by("?")[:5]

        commentsForm = CreateCommentVideosFrom()

        EditVideos = Videos.objects.get(id = pk)

        vidForm = CreateVideoFrom(instance = EditVideos)

        if request.method == 'POST':
            
            vidForm = CreateVideoFrom(request.POST, request.FILES, instance = EditVideos) 

            if vidForm.is_valid():

                print("SAVING")
                
                vidForm.save()

                return redirect("mediaDetail", pk)

        print("VIDEO: ", VideosTable)
        context = { 
            "profileImg" : profileImg,
            "VideosTable" : VideosTable,
            "otherVid" : otherVid,
            "commentsForm" : commentsForm,
            "pk" : pk,
            "vidForm" : vidForm
        }
        return render (request, 'Pages/mediaDetail.html', context)
    
    else:
        return redirect("home")


@login_required(login_url='signIn')
@api_view(['GET'])
def commentsForEachVideo(request, pk):

    CommentsForVideos = CommentVideos.objects.filter(VideoID = pk)

    serializer = CommentVideosSerializer(CommentsForVideos, many=True)
    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def createCommentForVideo(request, pk):

    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>")

    if request.method == 'POST':

        serializer = CommentVideosSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            print("SAVING")
        else:
            print("NOT VALID")
            print("FORM ERRORS: ", serializer.errors)
            print(serializer.is_valid())

        return Response(serializer.data)


@login_required(login_url='signIn')
def deleteCommentForVideo (request, pk):
    delteThisComment = CommentVideos.objects.get(id = pk)
    delteThisComment.delete()
    return redirect("home")


@api_view(['GET'])
def ViewsForEachVideo(request, pk):

    viewsForEachVideo = Views.objects.filter(VideoID = pk)

    serializer = ViewsSerializer(viewsForEachVideo, many=True)
    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def saveViews(request, pk):

    if request.method == 'POST':

        serializer = ViewsSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            print("SAVING")
        else:
            print("NOT VALID")
            print("FORM ERRORS: ", serializer.errors)
            print(serializer.is_valid())

        return Response(serializer.data)

@login_required(login_url='signIn')
@api_view(['GET'])
def AllUsersWhoLoved(request, pk):

    viewsForEachVideo = LovedTheVideo.objects.filter(VideoID = pk)

    serializer = LovedTheVideoSerializer(viewsForEachVideo, many=True)

    return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def LovedButton(request, pk):

    lovedTable = LovedTheVideo.objects.filter(userID = request.user.id, VideoID = pk)

    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print ("COUNT: ", lovedTable.count()) 

    if lovedTable.count() == 0:
        if request.method == 'POST':

            serializer = LovedTheVideoSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()

                print("SAVING")
            else:
                print("NOT VALID")
                print("FORM ERRORS: ", serializer.errors)
                print(serializer.is_valid())

            return Response(serializer.data)

    else:
        return redirect("home")




@login_required(login_url='signIn')
def commentMedia(request, pk):
    
    commentExit = CommentVideos.objects.filter(id = pk).count()

    if(commentExit > 0):
        comment = CommentVideos.objects.get(id = pk)
        profileImg = Profile.objects.get(userID = request.user.id)

        profileCommenter = Profile.objects.get(userID = comment.userID)

        userName = User.objects.get(id = comment.userID.id)
        
        commetsTable = CommentVideos.objects.get(id = pk)

        editComments = CreateCommentVideosFrom(instance = commetsTable)

        userTable = User.objects.get(username = commetsTable.userID)

        if request.method == 'POST':
            
            editComments = CreateCommentVideosFrom(request.POST, request.FILES, instance = commetsTable) 

            if editComments.is_valid():

                print("SAVING")
                
                editComments.save()

                return redirect("commentMedia", pk)

        context = {
            "comment" : comment,
            "profileCommenter" :profileCommenter,
            "profileImg" : profileImg,
            "userName" : userName,
            "editComments" : editComments
        }

        return render (request, 'Pages/commentMedia.html', context)
    else:
        return redirect("home")


@login_required(login_url='signIn')
@api_view(['GET'])
def MessagesBetweenTwoUsers(request, SenderID, ReciverID):
    if request.user.is_authenticated:

        allMessages = Messages.objects.filter(Q(SenderID=SenderID, ReciverID=ReciverID) | Q(SenderID=ReciverID, ReciverID=SenderID)).order_by('Date')

        serializer = MessagesSerializer(allMessages, many=True)

        return Response(serializer.data)

    else:
        return redirect("signUp")


@login_required(login_url='signIn')
@api_view(['GET'])
def messagesInbox(request, pk):

    if request.user.id == int(pk):
        if request.user.is_authenticated:
            
            messagesFromUsers = Inbox.objects.filter(Q(SenderID=pk) | Q(ReciverId=pk)).order_by('Date')

            serializer = InboxSerializer(messagesFromUsers, many=True)

            return Response(serializer.data)

        else:
            return redirect("signUp") 
    else:
        return redirect("home") 


@login_required(login_url='signIn')
@api_view(['PUT'])
def updateWhenUserRecives(request, pk):

    allMessages = Messages.objects.get(id=pk)

    if request.method == 'PUT':
    
        serializer = MessagesSerializer(allMessages, data = request.data)

        if serializer.is_valid():
            serializer.save()

            print("SAVING")
        else:
            print("NOT VALID")
            print("FORM ERRORS: ", serializer.errors)
            print(serializer.is_valid())

        return Response(serializer.data)


@login_required(login_url='signIn')
def messagePage(request, pk):

    if request.user.is_authenticated:

        if request.user.id == int(pk):

            ProfileTable = Profile.objects.filter(userID = request.user.id).count()

            allInbox = Inbox.objects.all()


            if (ProfileTable > 0):
                
                profileImg = Profile.objects.get(userID = request.user.id)

                context = {
                    "profileImg": profileImg,
                    "allInbox" : allInbox
                }

                return render (request, 'Pages/Inbox.html', context)

            else:
                return redirect("profile", request.user.id)

        else:
            return redirect("home")

    else:
        return redirect("signUp")


    
@login_required(login_url='signIn')
def chatPage(request, SenderID, ReciverID):

    if request.user.is_authenticated:

        if request.user.id == int(SenderID) or request.user.id == int(ReciverID):

            if (SenderID == ReciverID):
                return redirect("home")

            else:

                ProfileTable = Profile.objects.filter(userID = request.user.id).count()
                inboxTable = Inbox.objects.filter(Q(SenderID=SenderID, ReciverId=ReciverID) | Q(SenderID=ReciverID, ReciverId=SenderID)).count()

                if (inboxTable == 0):
                    inboxID = 0;
                else:
                    inboxID = Inbox.objects.get(Q(SenderID=SenderID, ReciverId=ReciverID) | Q(SenderID=ReciverID, ReciverId=SenderID))
                    
                if (ProfileTable > 0):

                    userTable = User.objects.get(id = ReciverID)

                    MessagesFromToSendMessage = MessagesFrom()
                
                    profileImg = Profile.objects.get(userID = request.user.id)

                    profilTable = Profile.objects.get(userID = ReciverID)

                    profileSenderID = Profile.objects.get(userID = SenderID)

                    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("SENDERID: ", SenderID)
                    print("PROFILEID: ", profileSenderID.id)
                    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>")

                    context = {
                        "profileImg": profileImg,
                        "MessagesFromToSendMessage" : MessagesFromToSendMessage,
                        "userTable" : userTable,
                        "profilTable" : profilTable,
                        "SenderID": SenderID,
                        "ReciverID" : ReciverID,
                        "inboxTable" : inboxTable,
                        "profileSenderID" : profileSenderID,
                        "inboxID" : inboxID
                    }

                    return render (request, 'Pages/chat.html', context)

                else:
                    return redirect("profile", request.user.id)

        else:
            return redirect("home")

    else:
        return redirect("signUp")


@login_required(login_url='signIn')
@api_view(['POST'])
def createInbox(request, SenderID, ReciverID):
    
    inboxTable = Inbox.objects.filter(Q(SenderID=SenderID, ReciverId=ReciverID) | Q(SenderID=ReciverID, ReciverId=SenderID))

    if (inboxTable.count() == 0):
        if request.method == 'POST':
        
            serializer = InboxSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                print("SAVING")
            else:
                print("NOT VALID")
                print("FORM ERRORS: ", serializer.errors)
                print(serializer.is_valid())

            return Response(serializer.data)

    else:
        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("INBOX IS ALREADY CREATED")
        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        return Response(serializer.data)


@login_required(login_url='signIn')
@api_view(['POST'])
def sendMessage(request, SenderID, ReciverID):

    if request.method == 'POST':
        
        serializer = MessagesSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            print("SAVING")
        else:
            print("NOT VALID")
            print("FORM ERRORS: ", serializer.errors)
            print(serializer.is_valid())

        return Response(serializer.data)


@login_required(login_url='signIn')
def searchPost(request):

    search = request.GET.get("search") 

    print(len(search))

    if (len(search) == 0):
        return redirect("home")

    else:

        if request.method == "GET":

            print("SEARCH INPUT: ", search)

            SearchedPosts = posts.objects.filter(post__contains=search)

        profileImg = Profile.objects.get(userID = request.user.id)
        context = {
            "profileImg" : profileImg,
            "SearchedPosts" : SearchedPosts,
        }

        return render (request, 'Pages/SearchPost.html', context)


@login_required(login_url='signIn')
def searchPost(request):

    search = request.GET.get("search") 

    print(len(search))

    if (len(search) == 0):
        return redirect("home")

    else:

        if request.method == "GET":

            print("SEARCH INPUT: ", search)

            SearchedPosts = posts.objects.filter(post__contains=search)

        profileImg = Profile.objects.get(userID = request.user.id)
        context = {
            "profileImg" : profileImg,
            "SearchedPosts" : SearchedPosts,
        }

        return render (request, 'Pages/searchPost.html', context)


@login_required(login_url='signIn')
def SearchOpinion(request):
    search = request.GET.get("search") 

    print(len(search))

    if (len(search) == 0):
        return redirect("home")

    else:

        print("SEARCH INPUT: ", search)

        profileImg = Profile.objects.get(userID = request.user.id)
    
        SearchedOpinion = Opinions.objects.filter(opinion__icontains=search)

        context = {
            "profileImg" : profileImg,
            "SearchedOpinion" : SearchedOpinion,
        }

        return render (request, 'Pages/SearchOpinion.html', context)


@login_required(login_url='signIn')
def SearchMedia(request):
    search = request.GET.get("search") 

    print(len(search))

    if (len(search) == 0):
        return redirect("home")

    else:

        print("SEARCH INPUT: ", search)

        profileImg = Profile.objects.get(userID = request.user.id)
    
        SearchMedia = Videos.objects.filter(videoTitle__icontains=search)

        context = {
            "profileImg" : profileImg,
            "SearchMedia" : SearchMedia,
        }

        return render (request, 'Pages/SearchMedia.html', context)