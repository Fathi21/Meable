window.addEventListener('load', (event) => {

    var numbersEyes = document.querySelector(".numbersEyes")
    var urlPageID = document.querySelector("#userWaslookedID")

    function Eyes() {
        var url = "http://127.0.0.1:8000/eyesForEachUser/" + urlPageID.value + "/"

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((eyes) => {

                var NumOfEyes = numeral(Object.keys(eyes).length).format('0a');

                numbersEyes.innerHTML = NumOfEyes

            });

    }


    Eyes()


});