window.addEventListener('load', (event) => {

    console.log("CONNECTED")

    var showAllPosts = document.querySelector(".ALLpostforEachUser")
    var showAllOpinions = document.querySelector(".ALLOpinionsforEachUser").style.display = 'none';
    var showAllVid = document.querySelector(".ALLVidforEachUser").style.display = 'none';

    var activeWhenClicked1 = document.querySelector(".activeWhenClicked1")
    var activeWhenClicked2 = document.querySelector(".activeWhenClicked2")
    var activeWhenClicked3 = document.querySelector(".activeWhenClicked3")

    activeWhenClicked1.addEventListener("click", function(e) {

        var showAllPosts = document.querySelector(".ALLpostforEachUser").style.display = 'block';
        var showAllVid = document.querySelector(".ALLVidforEachUser").style.display = 'none';
        var showAllOpinions = document.querySelector(".ALLOpinionsforEachUser").style.display = 'none';

    })


    activeWhenClicked2.addEventListener("click", function(e) {
        var showAllPosts = document.querySelector(".ALLpostforEachUser").style.display = 'none';
        var showAllVid = document.querySelector(".ALLVidforEachUser").style.display = 'none';
        var showAllOpinions = document.querySelector(".ALLOpinionsforEachUser").style.display = 'block';

    })

    activeWhenClicked3.addEventListener("click", function(e) {
        var showAllPosts = document.querySelector(".ALLpostforEachUser").style.display = 'none';
        var showAllVid = document.querySelector(".ALLVidforEachUser").style.display = 'block';
        var showAllOpinions = document.querySelector(".ALLOpinionsforEachUser").style.display = 'none';

    })

});