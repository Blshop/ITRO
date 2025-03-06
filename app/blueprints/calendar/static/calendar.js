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

let current_year = JSON.parse(localStorage.getItem('year')) === null ? current_date.getFullYear() : JSON.parse(localStorage.getItem('year'));
let documents = {}


//  container_variables
let current_year_el = document.querySelector('.current-year')
let calendar_container = document.querySelector('.calendar-container')
let previous_btn = document.querySelector('.previous')
let next_btn = document.querySelector('.next')
const unit_selectBtn = document.querySelector(".unit-selection .select-btn")
const doc_selectBtn = document.querySelector(".document-selection .select-btn")


let active_units = []
let active_document_types = []

//  event listeners

previous_btn.addEventListener('click', () => {
    current_year--
    localStorage.setItem('year', JSON.stringify(current_year));
    load_calendar(current_year)
})
next_btn.addEventListener('click', () => {
    current_year++
    localStorage.setItem('year', JSON.stringify(current_year));
    load_calendar(current_year)
})


function load_calendar(current_year) {
    loadState()
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

    documents = await load_documents(active_units, active_document_types)
    for (const doc of documents) {
        let day = document.querySelector("[date='" + doc.date_creation + "']")
        day.style.backgroundColor = "lightgreen"
        let p = day.firstChild
        let span = day.querySelector('span.tooltip')
        console.log(span)
        if (span === null) {
            span = document.createElement('span')
        }
        if (doc.period == 'ежедневный') {
            doc.period = "Ремонт"
        }
        let toolP = document.createElement('p')
        span.appendChild(toolP)
        toolP.textContent = doc.unit + " " + doc.period + " "
        let i = document.createElement('i')
        i.setAttribute('doc_id', doc.document_id)
        i.addEventListener('click', (e) => {
            e.stopPropagation()
            edit_document(e.target.getAttribute('doc_id'))
        })
        i.classList.add('fa')
        i.classList.add("fa-edit")
        toolP.appendChild(i)
        span.classList.add('tooltip')
        toolP.setAttribute('path-to-file', doc.document_path)
        toolP.addEventListener('click', (e) => {
            e.stopPropagation()
            load_document(e.target.getAttribute('path-to-file'))
        })

        let event_count = day.querySelector('span.event-count')
        console.log(event_count)
        if (event_count === null) {
            event_count = document.createElement('span')
            p = document.createElement('p')
            p.textContent = '1'
            event_count.classList.add('event-count')
            event_count.appendChild(p)
            day.appendChild(span)
            day.appendChild(event_count)
        }
        else {
            event_count.firstChild.textContent = Number(event_count.firstChild.textContent) + 1
        }

    }
}

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

function load_document(path) {

    // document.querySelector('iframe').src = '/units/reports/2026/Aquity/сервисное_обслуживание/2024-07-18_sdfds.pdf"2024/Clinac_iX/сервисное_обслуживание/2024-08-16_.pdf'
    const modal = document.querySelector('.modal-pdf-viewer')
    // console.log(path)
    openModal(modal)
    getData(path)
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

async function getData(path) {
    console.log(path)
    const url = `/calendar/load_document/${path}`;
    console.log(url)
    // const url = "/units/reports/2024/Clinac_iX/сервисное_обслуживание/2024-08-26_.pdf";
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


// async function getData() {
//     // const url = "/units/reports/" + this.getAttribute('path');
//     const url = "/units/reports/2024/Clinac_iX/сервисное_обслуживание/2024-08-26_.pdf";
//     fetch(url).then(function (response) {
//         return response.blob();
//     }).then(function (myBlob) {
//         var objectURL = URL.createObjectURL(myBlob);
//         document.querySelector('iframe').src = '';
//         document.querySelector('iframe').src = objectURL;
//         objectURL = URL.revokeObjectURL(myBlob);
//     })
// }

let unit_selections = document.querySelectorAll(".unit-selection .item")
let document_type_selections = document.querySelectorAll(".document-selection .item")
unit_selections.forEach((unit_selection) => {
    unit_selection.addEventListener('click', () => {
        let unit_id = unit_selection.getAttribute('unit_id')
        if (active_units.includes(unit_id)) {
            const index = active_units.indexOf(unit_id);
            if (index > -1) {
                active_units.splice(index, 1);
            }
            unit_selection.classList.remove('checked')
        }
        else {
            unit_selection.classList.add('checked')
            active_units.push(unit_id)

        }

        localStorage.setItem('units', JSON.stringify(active_units));
        load_calendar(current_year)
    })
})

document_type_selections.forEach((document_type_selection) => {
    document_type_selection.addEventListener('click', () => {
        let document_type_id = document_type_selection.getAttribute('document_type_id')
        if (active_document_types.includes(document_type_id)) {
            const index = active_document_types.indexOf(document_type_id);
            if (index > -1) {
                active_document_types.splice(index, 1);
            }
            document_type_selection.classList.remove('checked')
        }
        else {
            document_type_selection.classList.add('checked')
            active_document_types.push(document_type_id)

        }
        localStorage.setItem('documents', JSON.stringify(active_document_types));
        load_calendar(current_year)
    })
})



async function load_documents(unit, document_type) {
    console.log(unit)
    const data = new URLSearchParams();
    data.append('unit', unit);
    data.append('document_type', document_type);
    data.append('year', current_year);
    return fetch("/calendar/load_documents?" + data.toString())
        .then(response => response.json())
        .then(data => {
            return data
        })
}


async function qwe() {
    let data = await load_documents()
    console.log(data)
}


async function upload_document() {
    const data = prepare_for_upload()
    // const rawResponse = await fetch('/upload_document/post', {
    //     method: 'POST',
    //     headers: {
    //         'Accept': 'application/json',
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ a: 1, b: 'Textual content' })
    // });
    // const content = await rawResponse.json();

    console.log(data);
}


function prepare_for_upload() {
    return {
        'unit_id': document.querySelector('#unit').value
    }
}

upload_document()


// const items = document.querySelectorAll('.item');
// console.log(items)

// // Load the state from local storage
// loadState();

// // Event listener to save state when a checkbox is changed
// items.forEach(item => {
//     item.addEventListener('click', saveState);
// });

// function saveState() {
//     console.log('sdfsdfd')
//     const checkboxStates = {};
//     items.forEach(item => {
//         checkboxStates[item.textContent] = item.checked;
//     });
//     localStorage.setItem('checkboxStates', JSON.stringify(checkboxStates));
// }

function loadState() {
    active_units = JSON.parse(localStorage.getItem('units'));
    if (active_units === null) active_units = []
    active_document_types = JSON.parse(localStorage.getItem('documents'));
    if (active_document_types === null) active_document_types = []
    let all_units = document.querySelectorAll('.unit-selection .item')
    all_units.forEach(unit => {
        if (active_units.includes(unit.getAttribute('unit_id'))) {
            unit.classList.add('checked')
        }
    })
    let all_documents = document.querySelectorAll('.document-selection .item')
    all_documents.forEach(document => {
        if (active_document_types.includes(document.getAttribute('document_type_id'))) {
            document.classList.add('checked')
        }
    })
    console.log(all_units)
    console.log(active_units)
}
