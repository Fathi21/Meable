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

    var lovedButton = document.querySelector(".loved")
    var userID = document.querySelector("#userID")
    var VideoID = document.querySelector("#VideoID")
    var numOfLoved = document.querySelector(".numOfLoved")

    function RenderAllLoved() {

        var url = "http://127.0.0.1:8000/AllUsersWhoLoved/" + VideoID.value + "/";

        fetch(url)
            .then(response => {
                return response.json();
            })

        .then(loved => {

            console.log("LOVED: ", loved)

            numOfLoved.innerHTML = ""

            var count = numeral(Object.keys(loved).length).format('0a');

            numOfLoved.innerHTML += count


        })
    }

    RenderAllLoved()

    lovedButton.addEventListener("click", function(e) {

        e.preventDefault()
        lovedButton.style.color = "#17a2f2";
        var url = "http://127.0.0.1:8000/LovedButton/" + VideoID.value + "/";

        fetch(url, {
            method: 'POST',

            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'userID': userID.value, 'VideoID': VideoID.value })


        }).then(function(response) {

            RenderAllLoved()

        })

    })


});