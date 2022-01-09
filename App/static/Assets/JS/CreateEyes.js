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

    function saveData() {

        var userID = document.querySelector("#userID")
        var userWaslookedID = document.querySelector("#userWaslookedID")
        var ProfilID_forEyesTable = document.querySelector("#ProfilID_forEyesTable")

        var booleanToCheckIfThisYourOwnProfile = userID.value === userWaslookedID.value;

        if (booleanToCheckIfThisYourOwnProfile === false) {

            var url = "http://127.0.0.1:8000/CreateEyes/" + userWaslookedID.value + "/";

            fetch(url, {
                method: 'POST',

                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'UserFollowed': userWaslookedID.value, 'userID': userID.value, 'profile': ProfilID_forEyesTable.value })


            }).then(function(response) {



            })
        } else {}

    }

    saveData()

});