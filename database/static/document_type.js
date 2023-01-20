function edit(element) {
    var row = element.parentNode;
    var rowIndex = row.rowIndex;
    var tr = document.getElementsByTagName("tr")[rowIndex];
    var unit_type_desc = tr.getElementsByTagName("td")[1];
    document.getElementById('document_type_desc').value = unit_type_desc.innerHTML
    document.querySelectorAll('input[type=submit]')[0].value = "Исправить"
    document.querySelectorAll('form')[0].action = "/database/general_data/document_type/" + element.id
}