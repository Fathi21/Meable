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

    var userID = document.querySelector("#userID")
    var VideoID = document.querySelector("#VideoID")
    var commentsWrapper = document.querySelector(".commentsWrapper")
    var id_comment = document.querySelector("#id_comment")
    var theNumberOfComments = document.querySelector(".theNumberOfComments")
    var buttonToCreateNewComment = document.querySelector(".createNewComment")

    function renderComments(users) {
        commentsWrapper.innerHTML = ""

        var url = "http://127.0.0.1:8000/commentsForEachVideo/" + VideoID.value + "/";
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


                                    var item = '<div class="EachComment">' + '<div class="row">' + '<div class="col-3">' + '<span class="ImgProfile">' + '<a href="http://127.0.0.1:8000/profile/' + users[i].id + '/">' + '<img src="' + profile[j].profileImage + '"class="rounded-circle" alt="...">' + '</a>' + '</span>' + '</div>' + '<div class="col-6 commentBox">' + '<span class="NameOfThecommenter">' + '<a href="http://127.0.0.1:8000/profile/' + users[i].id + '/">' + users[i].first_name + ' ' + users[i].last_name + '</a>' + '</span>' + '</div>' + '<div class="col-3">' + '<span class="dateTime float-right">' + moment(comments[x].Date).fromNow() + '</span>' + '</div>' + '</div>' + '<div class="row">' + '<div class="col-12">' + '<a href="http://127.0.0.1:8000/commentMedia/' + comments[x].id + '/">' + '<p class="TheComment">' + comments[x].comment + '</p>' + '</a>' + '</div>' + '</div>' + '</div>';
                                    commentsWrapper.innerHTML += item

                                }
                            }
                        }
                    }
                }


                var NumOfComments = numeral(countComments).format('0a');


                theNumberOfComments.innerHTML = NumOfComments

            })

        })



    }



    function users() {

        var url = "http://127.0.0.1:8000/AllUsers";

        fetch(url)
            .then(response => {
                return response.json();
            })

        .then(users => {

            renderComments(users)
        })
    }

    users()


    buttonToCreateNewComment.addEventListener("click", function(e) {

        e.preventDefault()

        var url = "http://127.0.0.1:8000/createCommentForVideo/" + VideoID.value + "/";

        fetch(url, {
            method: 'POST',

            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'comment': id_comment.value, 'userID': userID.value, 'VideoID': VideoID.value })


        }).then(function(response) {



        })



        id_comment.value = ""

        users()
    })


});