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

    var disagreeButton = document.querySelectorAll(".fa-window-close")

    var userIDHiddenInput = document.querySelector("#userID")

    console.log(disagreeButton)

    for (var i = 0; i < disagreeButton.length; i++) {

        disagreeButton[i].addEventListener("click", function(e) {

            var OpinionID = e.target.value
            var userID = userIDHiddenInput.value

            console.log(OpinionID)
            console.log("USER ID", userID)

            var url = "http://127.0.0.1:8000/Disagree/" + OpinionID + "/";


            fetch(url, {
                method: 'POST',

                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'OpinionID': OpinionID, 'userID': userID })
            }).then(function(response) {


            })


        })

    }






});