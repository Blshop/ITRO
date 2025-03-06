import { Table } from '/static/js/shared/table.js'
document.querySelector('.deviation').addEventListener('click', () => { createTable('deviation') })
document.querySelector('.unit_category').addEventListener('click', () => { createTable('unit_category') })
document.querySelector('.main_parameter').addEventListener('click', () => { createTable('parameter', 'основные') })
document.querySelector('.sec_parameter').addEventListener('click', () => { createTable('parameter', 'вторичные') })
document.querySelector('.planning_parameter').addEventListener('click', () => { createTable('parameter', 'планирование') })


let active_menu = document.querySelector('.side-menu a[href="' + window.location.pathname + '"]');
if (active_menu) {
    active_menu.classList.add('active');
}

const tableData = {
    'deviation': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'deviation_id' },
            { 'data-type': 'text', 'data-name': "deviation_desc" }
        ],
        'tableHead': { 'id': 'id', 'deviation_desc': 'Отклонение' }
    },
    'unit_category': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'category_parameter_id' },
            { 'data-type': 'text', 'data-name': "unit_category_desc" }
        ],
        'tableHead': { 'id': 'id', 'unit_category_desc': 'Категория аппарата' }
    },
    'parameter': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'parameter_id' },
            { 'data-type': 'text', 'data-name': "parameter_desc" },
            { 'data-type': 'select', 'data-name': "deviation" }
        ],
        'tableHead': { 'id': 'id', 'parameter_desc': 'Параметр', 'deviation': "Отклонение" }
    }
}


function createTable(tableName, filter = '') {
    let table = document.querySelector('table')
    if (table) {
        table.parentNode.removeChild(table)
        new Table(url, tableName, tableData[tableName]['dataInfo'], tableData[tableName]['tableHead'], filter)
    }
    else new Table(url, tableName, tableData[tableName]['dataInfo'], tableData[tableName]['tableHead'], filter)
}

const url = '/settings/';
