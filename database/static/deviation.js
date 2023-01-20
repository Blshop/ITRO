function edit(element) {
    var row = element.parentNode;
    var rowIndex = row.rowIndex;
    var tr = document.getElementsByTagName("tr")[rowIndex];
    var deviation_value = tr.getElementsByTagName("td")[1];
    document.getElementById('deviation_value').value = deviation_value.innerHTML
    document.querySelectorAll('input[type=submit]')[0].value = "Исправить"
    document.querySelectorAll('form')[0].action = "/database/general_data/deviation/" + element.id
}