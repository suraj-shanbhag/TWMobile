var book = function(train){
    var source = window.getParameterByName('source')
    var destination = window.getParameterByName('destination')
    var day = window.getParameterByName('day')
    window.location = "http://127.0.0.1:5000/book/?source="
                       + source + "&destination="
                       + destination + "&day="
                       + day + "&time="
                       + train.time;
//    window.location = "http://127.0.0.1:5000/book/?source=BNG&destination=GOA&day=2017-09-01&time=12%3A00";
}