window.addEventListener('load', (event) => {

    var numbersFollowers = document.querySelector(".numbersFollowers")
    var numbersFollowing = document.querySelector(".numbersFollowing")
    var urlPageID = document.querySelector("#userWaslookedID")

    function following() {
        var url = "http://127.0.0.1:8000/followingForEachUser/" + urlPageID.value + "/"

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((Following) => {

                console.log("FOLLOWERS: ", Following)

                var NumOfFollowing = numeral(Object.keys(Following).length).format('0a');

                numbersFollowing.innerHTML = NumOfFollowing

            });

    }

    following()

    function followers() {

        var url = "http://127.0.0.1:8000/followersForEachUser/" + urlPageID.value + "/"

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((followers) => {

                console.log("FOLLOWERS: ", followers)

                var NumOfFollowers = numeral(Object.keys(followers).length).format('0a');

                numbersFollowers.innerHTML = NumOfFollowers

            });
    }

    followers()

});