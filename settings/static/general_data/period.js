function edit(element) {
    var row = element.parentNode;
    var rowIndex = row.rowIndex;
    var tr = document.getElementsByTagName("tr")[rowIndex];
    var period_desc = tr.getElementsByTagName("td")[1];
    var days_number = tr.getElementsByTagName("td")[2];
    document.getElementById('period_desc').value = period_desc.innerHTML
    document.getElementById('days_number').value = days_number.innerHTML
    document.querySelectorAll('input[type=submit]')[0].value = "Исправить"
    document.querySelectorAll('form')[0].action = "/database/general_data/period/" + element.id
}