function setupMenuActiveHighlight() {
    var div = document.getElementById("menu");
    var children = div.getElementsByClassName("menu_item");
    for (var i = 0; i < children.length; i++) {
        var child = children[i];
        child.addEventListener("click", function() {
            var current = div.getElementsByClassName("current_page_item")[0];
            current.className = current.className.replace(" current_page_item", "");
            this.className += " current_page_item";
        });
    }
}

function setupAccordions() {
    var accordions = document.getElementsByClassName("accordion");
    for (var i = 0; i < accordions.length; i++) {
        var tabs = accordions[i].getElementsByClassName("accordion_tab");
        for (var j = 0; j < tabs.length; j++) {
            var tab = tabs[j];
            tab.addEventListener("click", function() {
                this.classList.toggle("active");
                var panel = this.nextElementSibling;
                panel.style.display = (panel.style.display == "block") ? "none" : "block";

                if (panel.style.maxHeight) {
                    panel.style.maxHeight = null;
                } else {
                    panel.style.maxHeight = panel.scrollHeight + "px";
                }
            });
        }
    }
}

function setupDynamicContent() {
    setupMenuActiveHighlight();
    setupAccordions();
}

document.addEventListener("DOMContentLoaded", setupDynamicContent);