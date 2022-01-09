window.addEventListener('load', (event) => {

    var likeButton = document.querySelector(".fa-thumbs-up")

    var postID = document.querySelector("#postID");

    var numOfLikesinnerHTML = document.querySelector("#countLikes");

    CountTheLikes()

    function CountTheLikes() {

        var url = 'http://127.0.0.1:8000/AllLikes/' + postID.value + '/'

        var countLikes = 0

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((likes) => {
                numOfLikesinnerHTML.innerHTML = ""

                for (i in likes) {
                    countLikes += 1;
                }

                var NumOfLikes = numeral(countLikes).format('0a');

                numOfLikesinnerHTML.innerHTML += NumOfLikes

            });

    }

    CountTheLikes()

    CountTheLikes()


    likeButton.addEventListener("click", function(e) {

        var likeButton = document.querySelector(".fa-thumbs-up").style.color = "#28a745";
        var dislikeButton = document.querySelector(".fa-thumbs-down").style.color = "#000000";

        CountTheLikes()

        CountTheLikes()

        CountTheDisLikes()

        CountTheDisLikes()


    })

    var dislikeButton = document.querySelector(".fa-thumbs-down")
    var numOfDisLikesinnerHTML = document.querySelector("#countDisLikes");

    CountTheDisLikes()

    function CountTheDisLikes() {

        var url = 'http://127.0.0.1:8000/dislikeForAllPost/' + postID.value + '/'

        var countDisLikes = 0

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((dislikes) => {
                numOfDisLikesinnerHTML.innerHTML = ""

                for (i in dislikes) {
                    countDisLikes += 1;
                }

                var NumOfLikes = numeral(countDisLikes).format('0a');

                numOfDisLikesinnerHTML.innerHTML += NumOfLikes



            });

    }


    CountTheDisLikes()

    CountTheDisLikes()

    dislikeButton.addEventListener("click", function(e) {

        var likeButton = document.querySelector(".fa-thumbs-up").style.color = "#000000";
        var dislikeButton = document.querySelector(".fa-thumbs-down").style.color = "#dc3545";


        CountTheDisLikes()

        CountTheDisLikes()

        CountTheLikes()

        CountTheLikes()

    })




});