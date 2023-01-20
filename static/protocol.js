function daily(id) {

    // alert(id);
    // window.open("/daily", '_blank');
}

const cells = document.querySelectorAll('td');
cells.forEach(cell => { cell.addEventListener('click', function () { activate_cell(cell) }) })
// () =>
// console.log("Row index: " + cell.closest('tr').rowIndex + " | Column index: " + cell.cellIndex));
// });

const units = {}
function activate_cell(cell) {
    let unit = all_units[cell.closest('tr').rowIndex - 1]
    let period = all_periods[cell.cellIndex - 1]
    if (cell.classList.contains("active")) {
        to_print[unit] = to_print[unit].filter(item => item !== period)
    }
    else {
        if (unit in to_print) {
            to_print[unit].push(period)
        }
        else {
            console.log('else')
            to_print[unit] = [period]
        }
    }
    cell.classList.toggle("active")
    console.log(to_print)
}

let to_print = {}


function printa() {
    fetch("/daily", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(to_print)
    }).then(res => {
        console.log("Request complete! response:", res);
    });
    window.open("/daily", '_blank');
}

document.getElementById('print').addEventListener('click', printa)