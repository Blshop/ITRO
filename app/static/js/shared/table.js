export class Table {
    constructor(url, tableName, dataInfo, tableHead, filter) {
        this.url = url
        this.tableName = tableName
        this.dataInfo = dataInfo
        this.tableHead = tableHead
        this.data = null
        this.columnNumber = dataInfo.length
        this.activeEdit = false
        this.filter = filter
        this.#initialize()
        this.prepare_for_edit = this.prepare_for_edit.bind(this)
        this.createAddRow = this.createAddRow.bind(this)
        this.save_to_server = this.save_to_server.bind(this)
        this.cancel_changes = this.cancel_changes.bind(this)
    }

    async #initialize() {
        this.data = await this.#fetchData(this.url + 'load_data?table_name=' + this.tableName + '&filter=' + this.filter)
        if (this.data) this.createTable()
        else console.log('Failed to fetch data.')
    }

    #fetchData = async (url) => {
        const response = await fetch(url)
        const data = await response.json()
        console.log(data)
        return data
    }


    createTable = async () => {
        const container = document.querySelector('.table-container')
        const table = document.createElement('table')
        container.appendChild(table)
        let thead = table.createTHead()
        let row = await this.createRow(thead, this.tableHead)
        row.firstChild.textContent = '№ пп'
        let tbody = document.createElement('tbody')
        table.appendChild(tbody)
        row = await this.createRow(tbody)
        row.addEventListener('dblclick', this.prepare_for_edit)
        for (let i = 0; i < this.data.length; i++) {
            let row = await this.createRow(tbody, this.data[i])
            row.firstChild.textContent = i + 1
            row.addEventListener('dblclick', this.prepare_for_edit)
        }
    }

    async prepare_for_edit(e) {
        if (this.activeEdit) return
        this.activeEdit = true
        e.stopPropagation()
        const rowNumber = Number(e.currentTarget.firstChild.textContent)
        let row = e.currentTarget.parentElement.insertRow(rowNumber + 1)
        e.currentTarget.classList.add('hidden')
        row.classList.add('edit')
        let cells = Array.from(e.currentTarget.querySelectorAll('td'))
        this.createAddRow(row, cells)
    }

    async createAddRow(row, cells) {
        row.insertCell()
        for (let i = 1; i < this.dataInfo.length; i++) {
            if (this.dataInfo[i]['data-type'] === 'text') {
                let cell = row.insertCell()
                cell.textContent = cells[i].textContent
                cell.setAttribute('contenteditable', 'true')
            }
            else if (this.dataInfo[i]['data-type'] === "select") {
                let cell = row.insertCell()
                let select = document.createElement("select")
                let option = document.createElement('option')
                option.value = ''
                select.append(option)
                let data = await this.#fetchData(this.url + 'load_data?table_name=' + this.dataInfo[i]['data-name'])
                for (let item of data) {
                    let option = document.createElement('option')
                    option.value = JSON.stringify(item)
                    option.textContent = item[this.dataInfo[i]['data-name'] + '_desc']
                    select.append(option)
                    if (option.textContent === cells[i].textContent) option.selected = true
                }
                cell.appendChild(select)
                select.addEventListener('oninput', () => {
                    this.filterOptions(this)
                })
            }
        }
        row.append(this.#createToolbar())
    }

    #createToolbar() {
        let toolbar = document.createElement('div')
        toolbar.classList.add('toolbar')
        let add_btn = document.createElement('button')
        add_btn.classList.add('add-btn')
        add_btn.textContent = "Добавить"
        add_btn.addEventListener('click', this.save_to_server)
        let cancel_btn = document.createElement('button')
        cancel_btn.classList.add('cancel-btn')
        cancel_btn.textContent = "Отмена"
        cancel_btn.addEventListener('click', this.cancel_changes)
        toolbar.append(add_btn, cancel_btn)
        return toolbar
    }

    async cancel_changes(e) {
        e.stopPropagation()
        let row = e.currentTarget.closest('tr')
        row.previousElementSibling.classList.remove('hidden')
        await row.parentNode.removeChild(row)
        this.activeEdit = false
    }

    async createRow(container, data = {}) {
        let row = container.insertRow()
        row.setAttribute('data-id', data[this.tableName + "_id"])
        for (let i = 0; i < this.columnNumber; i++) {
            let cell = row.insertCell()
            cell.setAttribute('data-name', this.dataInfo[i]['data-name'])
            cell.textContent = data[this.dataInfo[i]['data-name']]
        }
        return row
    }

    async save_to_server(e) {
        let data = {}
        let editRow = e.currentTarget.closest('tr')
        let editCells = editRow.querySelectorAll('td')
        let previousRow = editRow.previousElementSibling
        previousRow.classList.remove('hidden')
        let previousCells = previousRow.querySelectorAll('td')
        if (Number(editRow.previousElementSibling.getAttribute('data-id'))) {
            data[this.tableName + "_id"] = Number(editRow.previousElementSibling.getAttribute('data-id'))
        }
        else {
            let clonedRow = previousRow.cloneNode(true)
            previousRow.parentNode.insertBefore(clonedRow, previousRow)
            clonedRow.addEventListener('dblclick', this.prepare_for_edit)
            previousRow.classList.add('new')
            previousRow.removeEventListener('dblclick', this.prepare_for_edit)
        }
        for (let i = 1; i < editCells.length; i++) {
            if (editCells[i].textContent == '') continue
            if (this.dataInfo[i]['data-type'] === 'text') {
                data[this.dataInfo[i]['data-name']] = editCells[i].textContent
                previousCells[i].textContent = editCells[i].textContent
            }
            else if (this.dataInfo[i]['data-type'] === 'select') {
                let select = editCells[i].firstChild
                let selectOption = select.options[select.selectedIndex]
                if (selectOption.value != "") data[this.dataInfo[i]['data-name']] = JSON.parse(select.value)
                previousCells[i].textContent = selectOption.textContent
            }
        }
        editRow.parentNode.removeChild(editRow)
        this.activeEdit = false
        this.addRowNumbers()
        console.log(data)
        this.sendDataToServer(data)
    }

    addRowNumbers() {
        const tbody = document.querySelector('tbody')
        const rows = tbody.getElementsByTagName('tr')
        for (let i = 1; i < rows.length; i++) {
            const firstCell = rows[i].firstChild
            firstCell.textContent = i
        }
    }

    async sendDataToServer(data) {
        try {
            const response = await fetch(this.url + 'upload_data?table_name=' + this.tableName + '&filter=' + this.filter, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const responseData = await response.json();
            console.log('Success:', responseData);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    filterOptions(selectElement) {
        const filter = selectElement.value.toLowerCase();
        const options = selectElement.options;

        for (let i = 0; i < options.length; i++) {
            const option = options[i];
            const text = option.text.toLowerCase();
            if (text.includes(filter)) {
                option.style.display = '';
            } else {
                option.style.display = 'none';
            }
        }
    }
}