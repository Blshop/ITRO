import { Table } from '/static/js/shared/table.js'
import { url } from './settings.js'
document.querySelector('.document_type').addEventListener('click', () => { createTable('document_type') })
document.querySelector('.organization').addEventListener('click', () => { createTable('organization') })

const tableData = {
    'document_type': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'document_type_id' },
            { 'data-type': 'text', 'data-name': "document_type_desc" }
        ],
        'tableHead': { 'id': 'id', 'document_type_desc': 'Тип документа' }
    },
    'organization': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'organization_id' },
            { 'data-type': 'text', 'data-name': "organization_desc" }
        ],
        'tableHead': { 'id': 'id', 'organization_desc': 'Организация' }
    },
}


function createTable(tableName) {
    let table = document.querySelector('table')
    if (table) {
        table.parentNode.removeChild(table)
        new Table(url, tableName, tableData[tableName]['dataInfo'], tableData[tableName]['tableHead'])
    }
    else new Table(url, tableName, tableData[tableName]['dataInfo'], tableData[tableName]['tableHead'])
}

