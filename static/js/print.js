function printDiv(divName) {
    var printContents = document.getElementById(divName).innerHTML;
    var originalContents = document.body.innerHTML;
    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}

function mail(divName){
    var printContents = document.getElementById(divName);
    var originalContents = document.body.innerHTML;
    var email = document.getElementsByTagName('input')['email'].value;
    document.body.innerHTML = printContents;
    window.location.href="mailto:" + email + "?subject="+document.title+"&body="+printContents.innerText;
    document.body.innerHTML = originalContents;
}