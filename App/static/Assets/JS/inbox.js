window.addEventListener('load', (event) => {

    var currentUser = document.querySelector("#currentUser")
    var inboxWraper = document.querySelector(".inboxWraper")
    console.log("CURRENT USER: ", currentUser.value)


    function inbox() {
        inboxWraper.innerHTML = ""

        var url = 'http://127.0.0.1:8000/messagesInbox/' + currentUser.value + '/';

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((inbox) => {

                fetch('http://127.0.0.1:8000/AllUsers')
                    .then((response) => {
                        return response.json();
                    })
                    .then((users) => {

                        fetch('http://127.0.0.1:8000/AllProfile')
                            .then((response) => {
                                return response.json();
                            })
                            .then((profile) => {

                                for (i in inbox) {

                                    if (inbox[i].ReciverId !== parseInt(currentUser.value) && inbox[i].SenderID !== parseInt(currentUser.value)) {


                                        console.log("FOUND THE CURRENT USER")

                                    } else {
                                        console.log("NOT FOUND")

                                        for (u in users) {

                                            if (users[u].id != parseInt(currentUser.value)) {
                                                if (inbox[i].ReciverId === users[u].id || inbox[i].SenderID === users[u].id) {
                                                    // console.log("RECIVER: ", inbox[i].ReciverId)
                                                    // console.log("SENDER: ", inbox[i].SenderID)

                                                    for (p in profile) {

                                                        if (profile[p].userID === users[u].id) {

                                                            var item = "<a href='http://127.0.0.1:8000/chat/" + parseInt(currentUser.value) + "/" + users[u].id + "/'>" + "<span class='ImgInbox'>" +
                                                                '<img src="' + profile[p].profileImage + '" class="img-fluid" alt="Responsive image">' +
                                                                '</span>' + '<span class="NameInbox">' +
                                                                users[u].first_name + ' ' + users[u].last_name +
                                                                '</span>' + '<span class="dateInbox">' +
                                                                'Started: ' + moment(inbox[i].Date).fromNow() +
                                                                '</span>' + '<span class="lastMessage">' +
                                                                '<p>' +
                                                                'Click to send a message' +
                                                                '</p>' +
                                                                '</span>' + '</a>'

                                                            console.log(users[u].id)

                                                            inboxWraper.innerHTML += item

                                                        }

                                                    }


                                                }
                                            }
                                        }

                                    }


                                }







                            });
                    });


            });
    }

    inbox()







});