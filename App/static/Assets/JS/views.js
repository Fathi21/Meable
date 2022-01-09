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
    var WhoPosted = document.querySelector("#WhoPosted")
    var numOfViews = document.querySelector(".numOfViews")

    function saveData() {

        if (WhoPosted.value != userID.value) {
            var url = "http://127.0.0.1:8000/saveViews/" + VideoID.value + "/";

            fetch(url, {
                method: 'POST',

                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'userID': userID.value, 'VideoID': VideoID.value })


            }).then(function(response) {



            })
        } else {

        }

    }

    saveData()


    function numbOfViews() {
        var url = "http://127.0.0.1:8000/ViewsForEachVideo/" + VideoID.value + "/";

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((views) => {
                numOfViews.innerHTML = ""

                var count = numeral(Object.keys(views).length).format('0a');

                numOfViews.innerHTML += count
            });
    }

    numbOfViews()
});