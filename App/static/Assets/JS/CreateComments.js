window.addEventListener('load', (event) => {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    console.log("CONNECTED")

    var userID = document.querySelector("#userID")
    var postID = document.querySelector("#postID")
    var profileID = document.querySelector("#profileID")
    var id_comment = document.querySelector("#id_comment")
    var commentsWrapper = document.querySelector(".commentsWrapper")
    var theNumberOfComments = document.querySelector('.CountComments')
    var buttonToCreateNewComment = document.querySelector(".createNewComment")

    var formWrapper = document.querySelector(".commentFormWrapper")


    console.log(theNumberOfComments)

    function RenderAllcomentForEachPost(users) {
        commentsWrapper.innerHTML = ""

        var url = "http://127.0.0.1:8000/comments/" + postID.value + "/";

        var countComments = 0;
        fetch(url)
            .then(response => {
                return response.json();
            })

        .then(comments => {

            var url = "http://127.0.0.1:8000/AllProfile";

            fetch(url)
                .then(response => {
                    return response.json();
                })

            .then(profile => {

                for (i in users) {

                    for (x in comments) {

                        if (users[i].id == comments[x].userID) {
                            countComments += 1;
                            for (j in profile) {

                                if (profile[j].userID == users[i].id) {
                                    var item = '<div class="EachComment">' + '<div class="row">' + '<div class="col-3">' + '<span class="ImgProfile">' + '<a href="http://127.0.0.1:8000/profile/' + users[i].id + '/">' + '<img src="' + profile[j].profileImage + '"class="rounded-circle" alt="...">' + '</a>' + '</span>' + '</div>' + '<div class="col-6 commentBox">' + '<span class="NameOfThecommenter">' + '<a href="http://127.0.0.1:8000/profile/' + users[i].id + '/">' + users[i].first_name + ' ' + users[i].last_name + '</a>' + '</span>' + '</div>' + '<div class="col-3">' + '<span class="dateTime float-right">' + moment(comments[x].DateCommented).startOf('hour').fromNow() + '</span>' + '</div>' + '</div>' + '<div class="row">' + '<div class="col-12">' + '<a href="http://127.0.0.1:8000/comment/' + comments[x].id + '/">' + '<p class="TheComment">' + comments[x].comment + '</p>' + '</a>' + '</div>' + '</div>' + '</div>';
                                    console.log(moment(comments[x].DateCommented).startOf('hour').fromNow())
                                    commentsWrapper.innerHTML += item

                                }
                            }
                        }
                    }
                }

                console.log(countComments)

                var NumOfLikes = numeral(countComments).format('0a');


                theNumberOfComments.innerHTML = NumOfLikes

            })


        })


    }

    AllUsers()

    function AllUsers() {

        var url = "http://127.0.0.1:8000/AllUsers";

        fetch(url)
            .then(response => {
                return response.json();
            })

        .then(users => {

            RenderAllcomentForEachPost(users)


        })

    }


    buttonToCreateNewComment.addEventListener("click", function(e) {

        e.preventDefault()

        var url = "http://127.0.0.1:8000/CreateComments/" + postID.value + "/";

        fetch(url, {
            method: 'POST',

            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'comment': id_comment.value, 'userID': userID.value, 'postID': postID.value, 'profile': profileID.value })


        }).then(function(response) {



        })


        AllUsers()
        id_comment.value = ""


    })

});