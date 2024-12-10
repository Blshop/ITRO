// variables
const day_names = [
    'Пн',
    'Вт',
    'Ср',
    'Чт',
    'Пт',
    'Сб',
    'Вс'
]

const month_names = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь',
]

let holidays = []


let current_date = new Date()
let current_year = current_date.getFullYear()
let documents = {}


//  container_variables
let current_year_el = document.querySelector('.current-year')
let calendar_container = document.querySelector('.calendar-container')
let previous_btn = document.querySelector('.previous')
let next_btn = document.querySelector('.next')
const unit_selectBtn = document.querySelector(".unit-selection .select-btn")
const doc_selectBtn = document.querySelector(".document-selection .select-btn")


//  event listeners

previous_btn.addEventListener('click', () => {
    current_year--
    load_calendar(current_year)
})
next_btn.addEventListener('click', () => {
    current_year++
    load_calendar(current_year)
})


function load_calendar(current_year) {
    create_calendar(current_year)
    populate_calendar()
}


function create_calendar(current_year) {
    calendar_container.removeChild(calendar_container.firstChild)
    let month_container = document.createElement('div')
    month_container.classList.add('month-container')
    calendar_container.appendChild(month_container)
    current_year_el.innerText = current_year

    for (let month_number = 0; month_number < 12; month_number++) {
        let month = document.createElement('div')
        month.classList.add('month')
        let h3 = document.createElement('h3')
        h3.innerHTML = month_names[month_number]
        let days_caption = document.createElement('div')
        days_caption.classList.add('days-caption')
        let days = document.createElement('div')
        days.classList.add('days')
        month.appendChild(h3)
        days.appendChild(days_caption)
        month.appendChild(days)
        let start_date = new Date(current_year, month_number, 1).getDay()
        if (start_date == 0) {
            start_date = 7
        }
        let end_date = new Date(current_year, month_number + 1, 0).getDate() + start_date
        for (let i = 0; i < 7; i++) {
            let day = document.createElement('div')
            day.classList.add('day')
            day.innerHTML = day_names[i]
            // let p = document.createElement('p')
            // p.
            // day.appendChild(p)
            days_caption.appendChild(day)
        }
        for (let i = 1; i < end_date; i++) {

            let day = document.createElement('div')
            if (i >= start_date) {
                day.classList.add('day')
                day.innerText = i - start_date + 1
                // let p = document.createElement('p')
                // p.textContent =
                let current_date = new Date(current_year, month_number, day.textContent)
                if (current_date.getDay() == 6 || current_date.getDay() == 0) day.style.backgroundColor = 'lightgray';
                // day.appendChild(p)
                current_date.setDate(current_date.getDate() + 1)
                day.setAttribute('date', current_date.toISOString().substring(0, 10))
                day.addEventListener('click', (e) => {
                    console.log(this)
                    const modal = document.querySelector('.modal-document')
                    openModal(modal)
                    document.querySelector("#start_date").value = e.target.getAttribute('date')
                })
            }
            days.appendChild(day)
        }
        month_container.appendChild(month)
    }
}

async function populate_calendar() {
    holidays = generate_holidays(current_year)
    for (const holiday of holidays) {
        holiday.setDate(holiday.getDate() + 1)
        let day = document.querySelector("[date='" + holiday.toISOString().split('T')[0] + "']")
        day.style.backgroundColor = 'lightgray';
    }

    documents = await upload_word()
    for (const [key, value] of Object.entries(documents)) {
        let day = document.querySelector("[date='" + key + "']")
        day.style.backgroundColor = "lightgreen"
        let p = day.firstChild
        let span = document.createElement('span')
        if (value[1] == 'ежедневный') {

            value[1] = "Ремонт"
        }
        span.textContent = value + " "
        let i = document.createElement('i')
        i.addEventListener('click', (e) => {
            e.stopPropagation()
            edit_document()
        })
        i.classList.add('fa')
        i.classList.add("fa-edit")
        span.appendChild(i)
        span.classList.add('tooltip')
        span.setAttribute('path-to-file', '2024/Clinac_iX/сервисное_обслуживание/2024-08-16_.pdf')
        span.addEventListener('click', (e) => {
            e.stopPropagation()
            console.log('sdfsdfdf')
            load_document()
        })
        let event_count = document.createElement('span')
        p = document.createElement('p')
        p.innerHTML = '1'
        event_count.classList.add('event-count')
        event_count.appendChild(p)
        day.appendChild(span)
        day.appendChild(event_count)
    }
}

// let words_data = JSON.parse(
//     document.querySelector('meta[name="words"]').getAttribute('data-words')
// )
// for (const [key, value] of Object.entries(documents)) {
//     let day = document.querySelector("[date='" + key + "']")
//     day.style.backgroundColor = "lightgreen"
//     let p = day.firstChild
//     let span = document.createElement('span')
//     if (value[1] == 'ежедневный') {

//         value[1] = "Ремонт"
//     }
//     span.innerHTML = value + document.createElement('i').classList.add("fas fa-edit")
//     span.classList.add('tooltip')
//     span.setAttribute('path-to-file', '2024/Clinac_iX/сервисное_обслуживание/2024-08-16_.pdf')
//     let event_count = document.createElement('span')
//     p = document.createElement('p')
//     p.innerHTML = '1'
//     event_count.classList.add('event-count')
//     event_count.appendChild(p)
//     day.appendChild(span)
//     day.appendChild(event_count)
// }

async function upload_word() {
    return fetch("/calendar/load_info/" + current_year)
        .then(response => response.json())
        .then(data => {
            return data
        })
}

function makeEaste(year) {
    var a = (19 * (year % 19) + 15) % 30;
    var b = ((2 * (year % 4) + 4 * (year % 7) + 6 * a + 6) % 7);
    if (a + b > 10)
        var p = new Date(year, 3, a + b - 9, 0, 0, 0, 0);
    else
        p = new Date(year, 2, 22 + a + b, 0, 0, 0, 0);
    p.setDate(p.getDate() + 22);
    return p;
}
function generate_holidays(year) {
    holidays = []
    holidays.push(new Date(year, 0, 1))
    holidays.push(new Date(year, 0, 2))
    holidays.push(new Date(year, 0, 7))
    holidays.push(new Date(year, 2, 8))
    holidays.push(new Date(year, 4, 1))
    holidays.push(new Date(year, 4, 9))
    holidays.push(new Date(year, 6, 3))
    holidays.push(new Date(year, 10, 7))
    holidays.push(new Date(year, 11, 25))
    holidays.push(makeEaste(year))
    return holidays
}


load_calendar(current_year)

function load_document() {

    // document.querySelector('iframe').src = '/units/reports/2026/Aquity/сервисное_обслуживание/2024-07-18_sdfds.pdf"2024/Clinac_iX/сервисное_обслуживание/2024-08-16_.pdf'
    const modal = document.querySelector('.modal-pdf-viewer')
    openModal(modal)
    getData()
}

overlay.addEventListener('click', () => {
    const modal = document.querySelector('.modal-pdf-viewer')
    closeModal(modal)
})

function openModal(modal) {
    if (modal == null) return
    modal.classList.add('active')
    overlay.classList.add('active')

}

async function getData() {
    // const url = "/units/reports/" + this.getAttribute('path');
    const url = "/units/reports/2024/Clinac_iX/сервисное_обслуживание/2024-08-26_.pdf";
    fetch(url).then(function (response) {
        return response.blob();
    }).then(function (myBlob) {
        var objectURL = URL.createObjectURL(myBlob);
        document.querySelector('iframe').src = '';
        document.querySelector('iframe').src = objectURL;
        objectURL = URL.revokeObjectURL(myBlob);
    })
}


function closeModal(modal) {
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}

closeModal()
let modal = document.querySelector('.modal-pdf-viewer')


async function getData() {
    // const url = "/units/reports/" + this.getAttribute('path');
    const url = "/units/reports/2024/Clinac_iX/сервисное_обслуживание/2024-08-26_.pdf";
    fetch(url).then(function (response) {
        return response.blob();
    }).then(function (myBlob) {
        var objectURL = URL.createObjectURL(myBlob);
        document.querySelector('iframe').src = '';
        document.querySelector('iframe').src = objectURL;
        objectURL = URL.revokeObjectURL(myBlob);
    })
}