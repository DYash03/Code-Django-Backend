$("body").toggleClass(localStorage.toggled);
function dark() {
    if (localStorage.toggled == "dimdark") {
        $("body").removeClass("dimdark");
    }
    $("body").addClass("dark");
    localStorage.toggled = "dark";
}
function dimdark() {
    if (localStorage.toggled == "dark") {
        $("body").removeClass("dark");
    }
    $("body").addClass("dimdark");
    localStorage.toggled = "dimdark";
}
function light() {
    if (localStorage.toggled == "dark") {
        $("body").removeClass("dark");
        localStorage.toggled = " ";
    }
    else if (localStorage.toggled == "dimdark") {
        $("body").removeClass("dimdark");
        localStorage.toggled = " ";
    }
}