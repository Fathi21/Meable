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

    var userIDHiddenInput = document.querySelector("#userID")

    var UserFollowedID = document.querySelectorAll("#UserFollowedID")

    for (var i = 0; i < UserFollowedID.length; i++) {
        UserFollowedID[i].addEventListener("click", function(e) {

            var userFollowed = e.target.value
            var userID = userIDHiddenInput.value

            var url = "http://127.0.0.1:8000/Followers/" + userFollowed + "/"


            fetch(url, {
                method: 'POST',

                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'UserFollowed': userFollowed, 'userID': userID })
            }).then(function(response) {


            })
        })
    }





});