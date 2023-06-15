// -------------------------

const themeToggle = document.querySelector("#theme-toggle");
const icon = themeToggle.querySelector("i");

themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");

    const isDarkModeEnabled = document.body.classList.contains('dark-mode');
    localStorage.setItem('isDarkModeEnabled', isDarkModeEnabled);

    if (document.body.classList.contains("dark-mode")) {
        icon.classList.remove("fa-moon");
        icon.classList.add("fa-sun");
    } else {
        icon.classList.remove("fa-sun");
        icon.classList.add("fa-moon");
    }
});

const isDarkModeEnabled = localStorage.getItem('isDarkModeEnabled');

if (isDarkModeEnabled === 'true') {
    document.body.classList.add('dark-mode');
    icon.classList.remove("fa-moon");
    icon.classList.add("fa-sun");
} else {
    document.body.classList.remove('dark-mode');
    icon.classList.remove("fa-sun");
    icon.classList.add("fa-moon");
}


// -------------------------

const calculateButton = document.querySelector("#calculate-expression");

if (calculateButton) {
    calculateButton.addEventListener("click", () => {
        const result = document.getElementById("calculator-result");
        const expression = document.getElementById("expression");
        result.textContent = eval(expression.value);
    });
}

const clearButton = document.querySelector("#calculator-clear");

if (clearButton) {
    clearButton.addEventListener("click", () => {
        const result = document.getElementById("calculator-result");
        const expression = document.getElementById("expression");
        result.textContent = "";
        expression.value = "";
    });
}

// -------------------------

const printText = document.querySelector("#print-text");
const textExpression = document.querySelector("#text-expression");

if (printText) {
    printText.addEventListener("click", () => {
        const text = document.getElementById("text-result");
        text.textContent = textExpression.value;
    });
}

const clearText = document.querySelector("#text-clear");

if (clearText) {
    clearText.addEventListener("click", () => {
        const text = document.getElementById("text-result");
        text.textContent = "";
        textExpression.value = "";
    });
}

// -------------------------

const printName = document.querySelector("#print-name");
const nameExpression = document.querySelector("#name-expression");

if (printName) {
    printName.addEventListener("click", () => {
        const name = document.getElementById("name-result");
        let result = nameExpression.value
        let text = "";
    
        for (let i = 0; i < 3; i++) {
            text = text + result + "\n";
        }
    
        name.textContent = text;
    });
}

const clearName = document.querySelector("#name-clear");

if (clearName) {
    clearName.addEventListener("click", () => {
        const name = document.getElementById("name-result");
        name.textContent = "";
        nameExpression.value = "";
    });
}

// -------------------------

var todayDate = document.getElementById("today-date");

if (todayDate) {
    var date = new Date();
    var months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"];

    var day = date.getDate();
    var month = months[date.getMonth()];
    var year = date.getFullYear();

    var completeDate = day + " de " + month + ", " + year;

    todayDate.innerHTML = completeDate
}


// -------------------------

function changeColour() {
    document.getElementById("circle").style.backgroundColor = "rgb(6, 251, 100)";
}

function resetColour() {
    document.getElementById("circle").style.backgroundColor = "rgb(6, 55, 251)";
}

// -------------------------

window.addEventListener("scroll", revealText);

function revealText(){
    var reveals = document.querySelectorAll("section p");

    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var revealTop = reveals[i].getBoundingClientRect().top;
        var revealPoint = 150;

        if (revealTop < windowHeight - revealPoint) {
            reveals[i].classList.add("active");
        } else {
            reveals[i].classList.remove("active");
        }
    }
}