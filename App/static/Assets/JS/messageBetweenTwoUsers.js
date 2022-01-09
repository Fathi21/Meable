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
    var msg_history = document.querySelector(".msg_history")
    var msg_send_btn = document.querySelector(".msg_send_btn")
    var message = document.querySelector("#message")
    var profileSenderID = document.querySelector("#profileSenderID")
    var inboxID = document.querySelector("#inboxID")



    function showMessages() {
        msg_history.innerHTML = ""

        var url = "http://127.0.0.1:8000/MessagesBetweenTwoUsers/" + SenderID.value + "/" + ReciverID.value + "/";

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((messages) => {


                console.log(msg_history)

                for (m in messages) {

                    if (messages[m].ReciverID == ReciverID.value || messages[m].SenderID == SenderID.value) {
                        var MessageRead = ""



                        var senderMessages = '<div class="outgoing_msg">' +
                            '<div class="sent_msg">' +
                            '<p>' + messages[m].Message +
                            '</p>' +
                            '<span class="time_date">' + moment(messages[m].Date).fromNow() + '</span>' + '</div>' +
                            '</div>';

                        msg_history.innerHTML += senderMessages


                    } else {

                        if (messages[m].ReciverReadYet == true) {
                            MessageRead = '<i class="fas fa-eye read"></i>'
                        } else {
                            MessageRead = '<i class="fas fa-eye"></i>'
                        }
                        var reciverMessages = '<div class="incoming_msg">' +
                            '<div class="received_msg">' +
                            '<div class="received_withd_msg">' +
                            '<p>' + messages[m].Message + '</p>' +
                            '<span class="time_date">' + moment(messages[m].Date).fromNow() + ' | ' + MessageRead + '</span></div>' +
                            '</div>' +
                            '</div>'

                        msg_history.innerHTML += reciverMessages



                    }




                }


            });
    }


    showMessages()

    msg_send_btn.addEventListener("click", () => {
        var lenghtOfTheMessage = message.value
        if (lenghtOfTheMessage.length > 0) {
            var url = "http://127.0.0.1:8000/sendMessage/" + SenderID.value + "/" + ReciverID.value + "/";

            fetch(url, {
                method: 'POST',

                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'SenderID': SenderID.value, 'ReciverID': ReciverID.value, 'Message': message.value, 'profileID': profileSenderID.value, 'inboxID': inboxID.value })


            }).then(function(response) {
                showMessages()

            })

        } else {}


        message.value = ""



    });




});