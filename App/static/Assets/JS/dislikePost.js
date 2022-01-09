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

    var dislikeButton = document.querySelectorAll(".fa-thumbs-down")

    var userIDHiddenInput = document.querySelector("#userID")

    for (var i = 0; i < dislikeButton.length; i++) {

        dislikeButton[i].addEventListener("click", function(e) {

            var PostID = e.target.value
            var userID = userIDHiddenInput.value

            console.log(userID)
            var url = "http://127.0.0.1:8000/dislike/" + PostID + "/";

            fetch(url, {
                method: 'POST',

                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'postID': PostID, 'userID': userID })
            }).then(function(response) {




            })


        })
    }





});