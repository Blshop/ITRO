const rows = document.getElementsByClassName('data')
for (let row of rows) {
    row.addEventListener('click', load_data)
}

function load_data(e) {
    if (e.offsetX > this.offsetWidth) {
        openModalButton.click()
        var inputs = document.querySelectorAll('.input_box')
        console.log(inputs[0])
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].children[1].value = this.children[i + 1].innerHTML
        }
        document.querySelector('input[type="submit"]').value = "Обновить"
        document.querySelector('input[name="id"]').value = this.id
    }
}
