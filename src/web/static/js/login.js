const container = document.querySelector(".container");
const loginBtn = document.querySelector(".login-btn");

loginBtn.addEventListener("click", () => {
    container.classList.remove("active");
    window.location.href = "main.html";
});

document.addEventListener("DOMContentLoaded", (event) => {
});
