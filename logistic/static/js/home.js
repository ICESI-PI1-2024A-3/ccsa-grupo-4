const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    toogle = body.querySelector(".toggle"),
    //falta el search
    modeSwitch = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");

toogle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
})

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
        modeText.innerText = "Light mode"
    } else {
        modeText.innerText = "Dark mode"
    }
})


const searchInput = document.querySelector('#search-input');
searchInput.addEventListener('keypress', function (event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        filterTable();
    }
});

function filterTable() {
    const searchInput = document.querySelector('#search-input');
    const searchQuery = searchInput.value.toLowerCase();
    const tableRows = document.querySelectorAll('table tbody tr');

    tableRows.forEach(function (row) {
        const rowText = row.textContent.toLowerCase();
        if (rowText.includes(searchQuery)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}