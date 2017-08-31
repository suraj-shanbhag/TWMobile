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
    month = ("0" + month).slice(-2);
    var year = today.getFullYear();
    day.setAttribute('min', year + '-' + month + '-' + date);
}