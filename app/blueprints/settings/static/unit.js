import { Table } from '/static/js/shared/table.js'
document.querySelector('.energy_type').addEventListener('click', () => { createTable('energy_type') })
document.querySelector('.energy').addEventListener('click', () => { createTable('energy') })
document.querySelector('.unit_type').addEventListener('click', () => { createTable('unit_type') })
document.querySelector('.unit').addEventListener('click', () => { createTable('unit') })


let active_menu = document.querySelector('.side-menu a[href="' + window.location.pathname + '"]');
if (active_menu) {
    active_menu.classList.add('active');
}

const tableData = {
    'energy_type': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'energy_type_id' },
            { 'data-type': 'text', 'data-name': "energy_type_desc" }
        ],
        'tableHead': { 'id': 'id', 'energy_type_desc': 'Тип энергии' }
    },
    'energy': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'energy_id' },
            { 'data-type': 'text', 'data-name': "energy_desc" },
            { 'data-type': 'select', 'data-name': "energy_type" },
            { 'data-type': 'text', 'data-name': "half_life" }
        ],
        'tableHead': { 'id': 'id', 'energy_desc': 'Энергия', 'energy_type': 'Тип энергии', 'half_life': 'Полураспад' }
    },
    'unit_type': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'unit_type_id' },
            { 'data-type': 'text', 'data-name': "unit_type_desc" },
            { 'data-type': 'select', 'data-name': "energy_type" }
        ],
        'tableHead': { 'id': 'id', 'unit_type_desc': 'Тип аппарата', 'energy_type': "Тип энергии" }
    },
    'unit': {
        'dataInfo': [
            { 'data-type': 'text', 'data-name': 'unit_id' },
            { 'data-type': 'text', 'data-name': "unit_desc" },
            { 'data-type': 'text', 'data-name': "unit_sn" },
            { 'data-type': 'select', 'data-name': "unit_type" },
            { 'data-type': 'select', 'data-name': "unit_category" }
        ],
        'tableHead': { 'id': 'id', 'unit_desc': 'Наименование', 'unit_sn': 'Серийный номер', 'unit_type': 'Тип аппарата', 'unit_category': 'Категория аппарата' }
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
