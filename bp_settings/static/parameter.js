const rows = document.getElementsByClassName('data')
for (let row of rows) {
    row.addEventListener('click', load_data)
}

function load_data(e) {
    if (e.offsetX > this.offsetWidth) {
        openModalButton.click()
        document.querySelector('input[type="submit"]').value = "Обновить"
        document.querySelector('input[name="parameter_desc"]').value = this.children[1].innerHTML
        document.querySelector('select[name="deviation_desc"]').value = this.children[2].innerHTML
        document.querySelector('input[name="id"]').value = this.id
    }
}
