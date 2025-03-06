const cells = document.querySelectorAll('td');
columns = document.querySelectorAll('th')
rows = document.querySelectorAll('tr')
let tables = ['unit', 'sec-unit', 'planning-system']
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
    }).then(response => response.text())
        .then(html => {
            var newWindow = window.open();
            newWindow.document.write(html);
            newWindow.document.close();
        })
        .catch(error => console.error('Error:', error));

};
document.querySelector('button').addEventListener('click', preparePrint)

function preparePrint() {
    let toPrint = {}
    for (let table of tables) {
        toPrint[table] = {}
        let rows = document.querySelectorAll('.' + table)
        console.log(rows)
        let periods = document.querySelectorAll('th')
        for (let i = 0; i < rows.length; i++) {
            let unitDesc = rows[i].firstElementChild.textContent
            console.log(unitDesc)
            let cells = rows[i].querySelectorAll('td.active')
            toPrint[table][unitDesc] = []
            for (let cell of cells) {
                toPrint[table][unitDesc].push(periods[cell.cellIndex].textContent)
            }
        }
        console.log(toPrint)
    }

    printa(toPrint)
}

function print_document() {
    window.open("/documents/print", '_blank')
}

function select_all(e) {
    let cell_index = e.cellIndex
    for (let i = 1; i < rows.length; i++) {
        rows[i].cells[cell_index].classList.toggle('active')
    }
}