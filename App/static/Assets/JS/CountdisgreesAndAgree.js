window.addEventListener('load', (event) => {

    var agreeButton = document.querySelector(".fa-check-square")

    var countAgree = document.querySelector("#countAgree");

    CountTheAgree()

    function CountTheAgree() {

        var url = 'http://127.0.0.1:8000/AgreeForAllOpinions/' + agreeButton.value + '/'

        var numOfAgrees = 0

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((Agrees) => {
                countAgree.innerHTML = ""

                for (i in Agrees) {
                    numOfAgrees += 1;
                }

                var NumOfTheAgrees = numeral(numOfAgrees).format('0a');

                countAgree.innerHTML += NumOfTheAgrees

            });

    }

    CountTheAgree()

    CountTheAgree()

    agreeButton.addEventListener("click", function(e) {

        var agreeButton = document.querySelector(".fa-check-square").style.color = "#28a745";
        var DisagreeButton = document.querySelector(".fa-window-close").style.color = "#212529";

        CountTheAgree()

        CountTheAgree()

        CountTheDisAgree()

        CountTheDisAgree()


    })

    var DisagreeButton = document.querySelector(".fa-window-close");
    var countDisagrees = document.querySelector("#countDisagrees");

    CountTheDisAgree()

    function CountTheDisAgree() {

        var url = 'http://127.0.0.1:8000/DisagreeForAllOpinions/' + DisagreeButton.value + '/'

        var numOfDisAgrees = 0

        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((Disagrees) => {
                countDisagrees.innerHTML = ""

                for (i in Disagrees) {
                    numOfDisAgrees += 1;
                }

                var numOfDisAgreesNumeral = numeral(numOfDisAgrees).format('0a');

                countDisagrees.innerHTML = numOfDisAgreesNumeral


            });

    }


    CountTheDisAgree()

    CountTheDisAgree()



    DisagreeButton.addEventListener("click", function(e) {

        var agreeButton = document.querySelector(".fa-check-square").style.color = "#000000";
        var DisagreeButton = document.querySelector(".fa-window-close").style.color = "#dc3545";


        CountTheDisAgree()

        CountTheDisAgree()

        CountTheAgree()

        CountTheAgree()


    })

});