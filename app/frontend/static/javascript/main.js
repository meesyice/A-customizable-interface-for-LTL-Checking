
function text() {
    var text = document.getElementById("text");
    text.style.display = "block";
}

function clickA() {
    text();
    var a = document.getElementById("a");
    var b = document.getElementById("b");
    var c = document.getElementById("c");
    var d = document.getElementById("d");
    
   
    b.style.display = "none";
    c.style.display = "none";
    d.style.display = "none";
    a.style.display = "inline";    
 }


function clickAB() {
    text();
    var a = document.getElementById("a");
    var b = document.getElementById("b");
    var c = document.getElementById("c");
    var d = document.getElementById("d");

    c.style.display = "none";
    d.style.display = "none";
    a.style.display = "inline";
    b.style.display = "inline";
    
}


function clickABC() {
    text();
    var a = document.getElementById("a");
    var b = document.getElementById("b");
    var c = document.getElementById("c");
    var d = document.getElementById("d");

    d.style.display = "none";
    a.style.display = "inline";
    b.style.display = "inline";
    c.style.display = "inline";

}

function clickABCD() {
    text();
    var a = document.getElementById("a");
    var b = document.getElementById("b");
    var c = document.getElementById("c");
    var d = document.getElementById("d");

    a.style.display = "inline";
    b.style.display = "inline";
    c.style.display = "inline";
    d.style.display = "inline";
}


