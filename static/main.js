const openModalButton = document.querySelector('[data-modal-target]')
const overlay = document.getElementById('overlay')
overlay.addEventListener('click', () => {
    const modal = document.querySelector('.modal.active')
    closeModal(modal)
})


openModalButton.addEventListener('click', () => {
    const modal = document.querySelector(openModalButton.dataset.modalTarget)
    openModal(modal)
})

function openModal(modal) {
    if (modal == null) return
    document.querySelector('input[type="submit"]').value = "Добавить"
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal(modal) {
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
    const inputs = document.querySelectorAll("input[type='text']")
    inputs.forEach((input) => { input.value = '' })
    document.querySelector('input[type="submit"]').value = "Добавить"
}


const sidebar = document.querySelector(".sidebar");
const sidebarClose = document.querySelector("#sidebar-close");
const menu = document.querySelector(".menu-content");
const menuItems = document.querySelectorAll(".submenu-item");
const subMenuTitles = document.querySelectorAll(".submenu .menu-title");
// sidebarClose.addEventListener("click", () => sidebar.classList.toggle("close"));
menuItems.forEach((item, index) => {
    item.addEventListener("click", () => {
        menu.classList.add("submenu-active");
        item.classList.add("show-submenu");
        menuItems.forEach((item2, index2) => {
            if (index !== index2) {
                item2.classList.remove("show-submenu");
            }
        });
    });
});
subMenuTitles.forEach((title) => {
    title.addEventListener("click", () => {
        menu.classList.remove("submenu-active");
    });
});


let load_pdf = document.querySelectorAll("a[path]").forEach(link => link.addEventListener('click', getData))

// let iframe = document.querySelector('iframe')
// load_pdf.addEventListener('click', getData)

async function getData() {
    const url = "/units/reports/" + this.getAttribute('path');
    // const url = "/units/reports/2026/Aquity/сервисное_обслуживание/2024-07-18_sdfds.pdf";
    fetch(url).then(function (response) {
        console.log('HITt', response)
        return response.blob();
    }).then(function (myBlob) {
        console.log(myBlob);
        var objectURL = URL.createObjectURL(myBlob);
        document.querySelector('iframe').src = '';
        document.querySelector('iframe').src = objectURL;
        objectURL = URL.revokeObjectURL(myBlob);
    })
}