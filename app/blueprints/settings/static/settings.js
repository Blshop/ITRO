let active_menu = document.querySelector('.side-menu a[href="' + window.location.pathname + '"]');
let activeTab
if (active_menu) {
    active_menu.classList.add('active');
}
export const url = '/settings/';

document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        if (activeTab !== tab) tab.classList.add('active')
        if (activeTab !== undefined) activeTab.classList.remove('active')
        activeTab = tab
    })
})