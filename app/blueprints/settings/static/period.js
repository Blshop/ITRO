import { Table } from '/static/js/shared/table.js'

const tableData = {
    'period': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'period_id' },
            { 'data-type': 'text', 'data-name': "period_desc" },
            { 'data-type': 'text', 'data-name': "period_duration" }
        ],
        'tableHead': { 'id': 'id', 'period_desc': 'Период', 'period_duration': 'Длительность' }
    }
}

function createTable(tableName) {
    let table = document.querySelector('table')
    if (table) {
        table.parentNode.removeChild(table)
        new Table(url, tableName, tableData[tableName]['dataInfo'], tableData[tableName]['tableHead'])
    }
    else new Table(url, tableName, tableData[tableName]['dataInfo'], tableData[tableName]['tableHead'])
}

const url = '/settings/';
createTable('period')