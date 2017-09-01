var form = document.forms[0]

function validateForm() {
    var source = form["source"].value;
    var destination = form["destination"].value;
    if(source == destination){
        alert("Both Source and Destination can not be same!!");
        return false;
    }
    return true;
}

function setMinValues() {
    var day = form["day"];
    var today = new Date();
    var date = today.getDate();
    var month = parseInt(today.getMonth()) + 1;
    var year = today.getFullYear();
    month = ("0" + month).slice(-2);
    date = ("0" + date).slice(-2);
    year = ("000" + year).slice(-4);
    day.setAttribute('min', year + '-' + month + '-' + date);
}