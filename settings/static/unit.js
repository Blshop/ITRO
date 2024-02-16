function edit(element) {
    var rowJavascript = element.parentNode;
    var rowIndexJavascript = rowJavascript.rowIndex;
    var tr = document.getElementsByTagName("tr")[rowIndexJavascript];
    var unit_desc = tr.getElementsByTagName("td")[1];
    var unit_type_desc = tr.getElementsByTagName("td")[2];
    var serial_number = tr.getElementsByTagName("td")[3];
    document.getElementById('unit_desc').value = unit_desc.innerHTML
    document.getElementById('unit_type_desc').value = unit_type_desc.innerHTML
    document.getElementById('serial_number').value = serial_number.innerHTML
    document.querySelectorAll('input[type=submit]')[0].value = "Исправить"
    document.querySelectorAll('form')[0].action = "/database/unit/" + element.id
}