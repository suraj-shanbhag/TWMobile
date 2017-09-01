function calculateTotalCost(divId) {
    var div = document.getElementsByClassName(divId);
    var cost = parseFloat(div['cost'].value);
    var seat = parseFloat(div['seat'].value);
    var totalCost = div['total_cost'];
    totalCost.setAttribute("value", cost * seat);
}