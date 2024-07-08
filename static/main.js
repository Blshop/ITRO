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