function edit(element) {
    var rowJavascript = element.parentNode;
    var rowIndexJavascript = rowJavascript.rowIndex;
    var tr = document.getElementsByTagName("tr")[rowIndexJavascript];
    var parameter_desc = tr.getElementsByTagName("td")[1];
    var deviation_value = tr.getElementsByTagName("td")[2];
    document.getElementById('parameter_desc').value = parameter_desc.innerHTML
    document.getElementById('deviation_value').value = deviation_value.innerHTML
    document.querySelectorAll('input[type=submit]')[0].value = "Исправить"
    document.querySelectorAll('form')[0].action = "/database/parameter/" + element.id
}