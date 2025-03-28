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

unit_desc.addEventListener('change', async function () {
    while (document_type.options.length > 1) {
        document_type.remove(1);
    }
    const selectedValue = unit_desc.value;
    if (selectedValue) {
        try {
            const response = await fetch(`/calendar/load_document?unit_desc=${selectedValue}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            // Update the result div with the fetched data
            console.log(data)
            if (data.length > 1) {
                data.forEach(option => {
                    if (!optionAlreadyExists(document_type, option.document_type)) {
                        const newOption = document.createElement('option');
                        newOption.value = option.document_type;
                        newOption.textContent = option.document_type;
                        document_type.appendChild(newOption);
                        document_type.classList.remove('active')
                    }

                });
            }
            else {
                const option = data[0]
                const newOption = document.createElement('option');
                newOption.value = option.document_type;
                newOption.textContent = option.document_type;
                document_type.appendChild(newOption);
                newOption.selected = true
                document_type.classList.add('active')
                const event = new Event('change', {
                    bubbles: true,
                    cancelable: true
                });
                document_type.dispatchEvent(event);
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
});

document_type.addEventListener('change', async function () {
    while (organization_type.options.length > 1) {
        organization_type.remove(1);
    }
    while (period_desc.options.length > 1) {
        period_desc.remove(1);
    }
    const selectedValue = document_type.value;
    if (selectedValue) {
        try {
            const response = await fetch(`/calendar/load_organizations?organization_desc=${selectedValue}&unit_desc=${unit_desc.value}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            // Update the result div with the fetched data
            console.log(data)
            if (data.organizations.length > 1) {
                data.organizations.forEach(option => {
                    const newOption = document.createElement('option');
                    newOption.value = option.organization;
                    newOption.textContent = option.organization;
                    organization_type.appendChild(newOption);
                    organization_type.classList.remove('active')
                });
            }
            else {
                const option = data.organizations[0]
                const newOption = document.createElement('option');
                newOption.value = option.organization;
                newOption.textContent = option.organization;
                organization_type.appendChild(newOption);
                newOption.selected = true
                organization_type.classList.add('active')
                const event = new Event('change', {
                    bubbles: true,
                    cancelable: true
                });
                organization_type.dispatchEvent(event);
            }
            if (data.periods.length > 1) {
                data.periods.forEach(option => {
                    const newOption = document.createElement('option');
                    newOption.value = option.period;
                    newOption.textContent = option.period;
                    period_desc.appendChild(newOption);
                    period_desc.classList.remove('active')
                });
            }
            else {
                const option = data.periods[0]
                const newOption = document.createElement('option');
                newOption.value = option.period;
                newOption.textContent = option.period;
                period_desc.appendChild(newOption);
                newOption.selected = true
                period_desc.classList.add('active')
                const event = new Event('change', {
                    bubbles: true,
                    cancelable: true
                });
                period_desc.dispatchEvent(event);
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
});


function optionAlreadyExists(selectElement, value) {
    // Loop through all the options in the <select> element
    for (let option of selectElement.options) {
        if (option.value === value) {
            return true; // Option already exists
        }
    }
    return false; // Option does not exist
}