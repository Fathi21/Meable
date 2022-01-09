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

    var SenderID = document.querySelector("#SenderID")
    var ReciverID = document.querySelector("#ReciverID")
    var checkIfHasInbox = document.querySelector("#inboxTable")

    function saveinbox() {

        if (checkIfHasInbox.value == 0) {
            var url = "http://127.0.0.1:8000/createInbox/" + SenderID.value + "/" + ReciverID.value + "/";
            fetch(url, {
                method: 'POST',

                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'SenderID': SenderID.value, 'ReciverId': ReciverID.value })


            }).then(function(response) {

            })

            window.location.reload();
        }
    }



    saveinbox()



});