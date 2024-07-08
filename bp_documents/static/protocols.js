const cells = document.querySelectorAll('td');
columns = document.querySelectorAll('th')
rows = document.querySelectorAll('tr')
console.log(rows)
// cells.forEach(cell => {
//     cell.addEventListener('click', () =>
//         console.log("Row index: " + cell.closest('tr').rowIndex + " | Column index: " + cell.cellIndex));
// });
document.querySelector('.print').addEventListener('click', print_document)
function toggle_cell() {
    this.classList.toggle('active')
}

cells.forEach(cell => {
    cell.addEventListener('click', toggle_cell);
});

function printa(to_print) {
    fetch("/documents/print", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'data': to_print, 'date': document.querySelector('input[type="month"]').value })
    }).then(res => {
        console.log("Request complete! response:", res);
    });
    location.reload()
}
document.querySelector('button').addEventListener('click', select_active)
function select_active() {
    let active_cells = document.querySelectorAll('.active')
    console.log(active_cells)
    let to_print = {}
    for (let cell of active_cells) {
        if (columns[cell.cellIndex].textContent in to_print) {
            to_print[columns[cell.cellIndex].textContent].push(rows[cell.closest('tr').rowIndex].cells[0].textContent)
        }
        else {
            to_print[columns[cell.cellIndex].textContent] = [rows[cell.closest('tr').rowIndex].cells[0].textContent]
        }

    }
    console.log(to_print)
    printa(to_print)
}

function print_document() {
    window.open("/documents/print", '_blank')
}

function select_all(e) {
    let cell_index = e.cellIndex
    console.log(e.cellIndex)
    for (let i = 1; i < rows.length; i++) {
        rows[i].cells[cell_index].classList.toggle('active')
    }
}