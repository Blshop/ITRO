document.getElementById('add').addEventListener('click', add)
document.getElementById('cancel').addEventListener('click', cancel)
let rows = document.getElementsByClassName('data')
for (let row of rows) {
    row.addEventListener('click', load_data)
}

let width = document.querySelector('table').offsetWidth
console.log(typeof (width))
console.log(width.toString())
document.querySelector('#add-form').style.width = width.toString() + 'px'
document.querySelector('input').style.width = (width - 140).toString() + 'px'

function add() {
    document.querySelector('#add-form').style.display = "flex"
    document.querySelector('#add').style.display = "none"
}

function cancel() {
    document.querySelector('#add-form').style.display = "none"
    document.querySelector('#add').style.display = "inline-block"
}

function load_data(e) {
    if (e.offsetX > this.offsetWidth) {
        id = this.id
        console.log(id)
        add()
    }

}