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


