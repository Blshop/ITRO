const cells = document.querySelectorAll('td');
let columns = document.querySelectorAll('th')
let rows = document.querySelectorAll('tr')
let tables = ['unit', 'sec-unit', 'planning-system']
// cells.forEach(cell => {
//     cell.addEventListener('click', () =>
//         console.log("Row index: " + cell.closest('tr').rowIndex + " | Column index: " + cell.cellIndex));
// });
function toggle_cell() {
    this.classList.toggle('active')
}

cells.forEach(cell => {
    cell.addEventListener('click', toggle_cell);
});
let organization_btn = document.querySelector('.organization_btn')
let document_type_btn = document.querySelector('.document_type_btn')
let organization = document.querySelector('.organization')
let document_type = document.querySelector('.document_type')

organization_btn.addEventListener('click', () => {
    document_type.classList.remove('active')
    organization.classList.add('active')
})

document_type_btn.addEventListener('click', () => {
    document_type.classList.add('active')
    organization.classList.remove('active')
})

document.querySelector('.save').addEventListener('click', preparePrint)

function printa(document_data, organization_data) {
    fetch("/units/upload_associacion", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'document_data': document_data, 'organization_data': organization_data })
    }).then(response => response.text()).catch(error => console.error('Error:', error));

};

function preparePrint() {
    let document_data = {}
    let rows = document_type.querySelectorAll('tbody tr')
    let periods = document_type.querySelectorAll('th')
    for (let i = 0; i < rows.length; i++) {
        let doc_type = rows[i].firstElementChild.textContent
        let cells = rows[i].querySelectorAll('td.active')
        document_data[doc_type] = []
        for (let cell of cells) {
            document_data[doc_type].push(periods[cell.cellIndex].textContent)
        }
    }
    let organization_data = {}
    rows = organization.querySelectorAll('tbody tr')
    periods = organization.querySelectorAll('th')
    for (let i = 0; i < rows.length; i++) {
        let org_type = rows[i].firstElementChild.textContent
        let cells = rows[i].querySelectorAll('td.active')
        organization_data[org_type] = []
        for (let cell of cells) {
            organization_data[org_type].push(periods[cell.cellIndex].textContent)
        }
    }
    console.log(document_data, organization_data)
    printa(document_data, organization_data)
}



const fetchData = async (url) => {
    const response = await fetch(url);
    const data = await response.json();
    return data;
};

// Example usage
fetchData("/units/load_associacion").then(data => {
    fill_table(data);
}).catch(error => {
    console.error('Error fetching data:', error);
});

function fill_table(data) {
    let docs = data['documents']
    let orgs = data['organizations']
    for (let doc of docs) {
        {
            console.log(doc.document_type, doc.period)
            findDocs(doc.document_type, doc.period)
        }
    }
    for (let org of orgs) {
        {
            console.log(org.document_type, org.organization)
            findOrgs(org.document_type, org.organization)
        }
    }
}

function findDocs(rowId, columnHeader) {
    const rows = document_type.querySelectorAll('tbody tr');
    const headers = document_type.querySelectorAll('thead th');
    let columnIndex = -1;

    // Find the column index for the given column header
    headers.forEach((header, index) => {
        if (header.textContent === columnHeader) {
            columnIndex = index;
        }
    });

    // Find the <td> based on row data and column index
    rows.forEach(row => {
        if (row.firstElementChild.textContent === rowId && columnIndex !== -1) {
            const td = row.children[columnIndex];
            if (td) {
                td.classList.add('active') // Highlight the <td> element
            }
        }
    });
}

function findOrgs(rowId, columnHeader) {
    const rows = organization.querySelectorAll('tbody tr');
    const headers = organization.querySelectorAll('thead th');
    console.log(headers)
    let columnIndex = -1;

    // Find the column index for the given column header
    headers.forEach((header, index) => {
        if (header.textContent === columnHeader) {
            columnIndex = index;
        }
    });

    // Find the <td> based on row data and column index
    rows.forEach(row => {
        if (row.firstElementChild.textContent === rowId && columnIndex !== -1) {
            const td = row.children[columnIndex];
            if (td) {
                td.classList.add('active') // Highlight the <td> element
            }
        }
    });
}