function printDiv(divName) {
    var printContents = document.getElementById(divName).innerHTML;
    var originalContents = document.body.innerHTML;
    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}

function mail(){
    var ticket = document.getElementById('ticket');
    var messageContainer = document.getElementById('message');
    var form = document['forms'][0];
    var email = form['email'].value;
    form.setAttribute('hidden', true);
    ticket.setAttribute('hidden', true);
    messageContainer.hidden = false;
    var message = document.createElement('p');
    message.innerText = "Thank You For Booking Ticket With Us\n"
                         + "Ticket will be sent to email:- " + email;
    messageContainer.appendChild(message)
}