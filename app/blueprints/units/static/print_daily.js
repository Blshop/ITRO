const years = document.getElementsByClassName('year')
const months = document.getElementsByClassName('month')
const all_months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];

for (let month of months) {
    console.log(month)
    month.textContent = all_months[0]
    console.log(all_months[1])
}

const getDays = (year, month) => new Date(year, month, 0)
let myDate = new Date(2025, 1, 0)
const max_days = myDate.getDate()
console.log(max_days)
let holiday_1 = new Date(2026, 1, 1)
let holiday_2 = new Date(2026, 1, 7)
let holiday_3 = new Date(2025, 1, 2)
let tables = document.querySelectorAll('table')
let tbodies = document.querySelectorAll('tbody')
for (let table of tables) {
    if (table.classList.contains('daily')) {
        let tbody = table.getElementsByTagName('tbody')[0]
        for (let i = 0; i < max_days; i++) {
            let row = tbody.insertRow(i)
            myDate.setDate(i + 1)
            if (myDate.getDate() == holiday_1.getDate()) { row.style.backgroundColor = 'lightgray' }
            if (myDate.getDate() == holiday_2.getDate()) { row.style.backgroundColor = 'lightgray' }
            if (myDate.getDate() == holiday_3.getDate()) { row.style.backgroundColor = 'lightgray' }
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
    // if (table.classList.contains('weekly')) {
    //     let tbody = table.getElementsByTagName('tbody')[0]
    //     for (let j = 0; j < tbody.rows.length - 2; j++) {
    //         for (let i = 0; i < 5; i++) {
    //             tbody.rows[j].insertCell()
    //         }
    //     }
    // }
    // if (table.classList.contains('quartal')) {
    //     let tbody = table.getElementsByTagName('tbody')[0]
    //     for (let j = 0; j < tbody.rows.length - 2; j++) {
    //         for (let i = 0; i < 4; i++) {
    //             tbody.rows[j].insertCell()
    //         }
    //     }
    // }
    // if (table.classList.contains('monthly')) {
    //     let tbody = table.getElementsByTagName('tbody')[0]
    //     for (let j = 0; j < tbody.rows.length - 1; j++) {
    //         for (let i = 0; i < 1; i++) {
    //             tbody.rows[j].insertCell()
    //         }
    //     }
    // }
}
