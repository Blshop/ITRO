// flags

unit_f = false
document_type_f = false
organization_f = false
period_f = false
file_f = false
end_date_f = true

// variables
let unit_desc = document.querySelector('select[name="unit_desc"]')
let document_type = document.querySelector('select[name="document_type_desc"]')
let organization_type = document.querySelector('select[name="organization_desc"]')
let period_desc = document.querySelector('select[name="period_desc"]')
let path_to_doc = document.querySelector('input[name = "path"]')
let upload_label = document.querySelector('.upload-container label')
let end_date = document.querySelector('input[name="end_date"]')
let period = document.querySelector('#period')

unit_desc.addEventListener('change', () => {
    unit_desc.classList.add('active')
    unit_f = true
    activate_add()
})

document_type.addEventListener('change', () => {
    document_type.classList.add('active')
    document_type_f = true
    activate_add()
})

organization_type.addEventListener('change', () => {
    organization_type.classList.add('active')
    organization_f = true
    activate_add()
})

period_desc.addEventListener('change', () => {
    period_desc.classList.add('active')
    period_f = true
    activate_add()
})

path_to_doc.addEventListener('change', () => {
    if (path_to_doc.files[0].type === 'application/pdf') {
        path_to_doc.classList.add('active')
        file_f = true
        upload_label.classList.add('active')
        upload_label.textContent = 'Файл загружен'
        activate_add()
    }
    else {
        path_to_doc.value = ''
    }

})

end_date.addEventListener('change', () => {
    end_date.classList.add('active')
    end_date_f = true
    activate_add()
})

period.addEventListener('click', (e) => {
    if (e.target.checked) {
        end_date.classList.add('inactive')
        end_date.classList.remove('active')
        end_date.disabled = false
        end_date_f = false
    }
    else {
        end_date.classList.remove('active')
        end_date.classList.remove('inactive')
        end_date.disabled = true
        end_date.value = ""
        end_date_f = true
    }
    activate_add()
})

end_date.addEventListener('change', () => {
    end_date.classList.remove('inactive')
    end_date.classList.add('active')
    end_date_f = true
    activate_add()
})

overlay.addEventListener('click', () => {
    const modal = document.querySelector('.modal-document.active')
    closeModal(modal)
})

function openModal(modal) {
    if (modal == null) return
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal(modal) {
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')

    unit_desc.classList.remove('active')
    unit_desc.selectedIndex = 0
    document_type.classList.remove('active')
    document_type.selectedIndex = 0
    organization_type.classList.remove('active')
    organization_type.selectedIndex = 0
    period_desc.classList.remove('active')
    period_desc.selectedIndex = 0
    upload_label.classList.remove('active')
    path_to_doc.value = ''
    upload_label.textContent = 'загрузить файл'
    end_date.classList.remove('active')
    end_date.classList.remove('inactive')
    end_date.disabled = true
    end_date.value = ""
    period.checked = false

    unit_f = false
    document_type_f = false
    period_f = false
    file_f = false
    end_date_f = true
    document.querySelector('.modal-document input[type="submit"]').disabled = true
}

function activate_add() {
    console.log(unit_f, document_type_f, organization_f, end_date_f, file_f)
    if (unit_f && document_type_f && organization_f && end_date_f && file_f && period_f) {
        document.querySelector('.modal-document input[type="submit"]').classList.add('active')
        document.querySelector('.modal-document input[type="submit"]').disabled = false
    }
    else {
        document.querySelector('.modal-document input[type="submit"]').classList.remove('active')
        document.querySelector('.modal-document input[type="submit"]').disabled = true
    }
}