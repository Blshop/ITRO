import { Table } from '/static/js/shared/table.js'
const tableData = {
    'unit_parameter': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'unit_parameter_id' },
            { 'data-type': 'select', 'data-name': "parameter" },
            { 'data-type': 'select', 'data-name': "period" }
        ],
        'tableHead': { 'id': 'id', 'parameter': 'Параметр', 'period': 'Периодичность' }
    },
    'sec_unit_parameter': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'sec_unit_parameter_id' },
            { 'data-type': 'select', 'data-name': "sec_parameter" },
            { 'data-type': 'select', 'data-name': "period" }
        ],
        'tableHead': { 'id': 'id', 'sec_parameter': 'Параметр', 'period': 'Периодичность' }
    },
    'planning_system': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'planning_system_id' },
            { 'data-type': 'select', 'data-name': "sec_parameter" },
            { 'data-type': 'select', 'data-name': "period" }
        ],
        'tableHead': { 'id': 'id', 'sec_parameter': 'Параметр', 'period': 'Периодичность' }
    }
}

function createTable(tableName, filter = '') {
    let table = document.querySelector('table')
    if (table) {
        table.parentNode.removeChild(table)
        new Table(url, tableName, tableData[tableName]['dataInfo'], tableData[tableName]['tableHead'])
    }
    else new Table(url, tableName, tableData[tableName]['dataInfo'], tableData[tableName]['tableHead'])
}

const url = '/units/';
createTable('unit_parameter')