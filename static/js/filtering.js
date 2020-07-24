function filterResults() {
    var filterCriteria = document.getElementById("notes-filter").value;
    var results = document.getElementById("results");
    var buttons = results.getElementsByTagName("button");
    for (var i = 0; i < buttons.length; i++) {
        var button = buttons[i];
        var noteName = button.innerHTML;
        if (noteName.indexOf(filterCriteria) > -1) {
            button.style.display = "";
        } else {
            var tagDiv = buttons[i].nextElementSibling;
            var tagUL = tagDiv.querySelector("#tags");
            var tags = tagUL.getElementsByTagName("li");
            button.style.display = "none";
            for (var j = 0; j < tags.length; j++) {
                if (tags[j].innerHTML.indexOf(filterCriteria) > -1) {
                    button.style.display = "";
                    break;
                }
            }
        }
        
    }
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("notes-filter").addEventListener("keyup", filterResults);
});