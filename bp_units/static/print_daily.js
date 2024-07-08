const years = document.getElementsByClassName('year')
const months = document.getElementsByClassName('month')
var myDate = new Date()
myDate.setFullYear(2024)
myDate.setMonth(7)
myDate.setDate(0)
const all_months = ["Январь", "February", "March", "April", "May", "June",
    "Июль", "August", "September", "October", "November", "December"];
// for (let year of years) {
//     year.innerHTML += myDate.getFullYear();
// }
for (let month of months) {
    console.log(month.innerHTML)
    month.innerHTML = all_months[Number(month.innerHTML) - 1]
}
let max_days = myDate.getDate()
let holiday = new Date(2024, 6, 3)
let tables = document.querySelectorAll('table')
let tbodies = document.querySelectorAll('tbody')
for (let table of tables) {
    if (table.classList.contains('daily')) {
        let tbody = table.getElementsByTagName('tbody')[0]
        for (let i = 0; i < max_days; i++) {
            let row = tbody.insertRow(i)
            myDate.setDate(i + 1)
            if (myDate.getDate() == holiday.getDate()) { row.style.backgroundColor = 'lightgray' }
            if (myDate.getDay() == 6 || myDate.getDay() == 0) row.style.backgroundColor = 'lightgray';
            let cell = row.insertCell()
            cell.innerHTML = i + 1
            for (let j = 1; j < tbody.parentNode.rows[0].cells.length; j++) {
                if (j == tbody.parentNode.rows[0].cells.length - 1) {
                    let last_cell = row.insertCell()
                    if (780 / tbody.parentNode.rows[0].cells.length < 70) {
                        last_cell.style.width = '70px'
                    } else if ((780 / tbody.parentNode.rows[0].cells.length < 110)) {
                        last_cell.style.width = '110px'
                    } else if ((780 / tbody.parentNode.rows[0].cells.length > 130)) {
                        last_cell.style.width = '130px'
                    }
                }
                else {
                    row.insertCell()
                }

            }
        };
    }
    if (table.classList.contains('weekly')) {
        let tbody = table.getElementsByTagName('tbody')[0]
        for (let j = 0; j < tbody.rows.length - 2; j++) {
            for (let i = 0; i < 5; i++) {
                tbody.rows[j].insertCell()
            }
        }
    }
    if (table.classList.contains('monthly')) {
        let tbody = table.getElementsByTagName('tbody')[0]
        for (let j = 0; j < tbody.rows.length - 1; j++) {
            for (let i = 0; i < 1; i++) {
                tbody.rows[j].insertCell()
            }
        }
    }
}
