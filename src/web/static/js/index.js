document.addEventListener("DOMContentLoaded", function() {
    const formElements = document.querySelectorAll("form label, form input, form button, menu");

    formElements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = 1;
            el.style.transition = "opacity 1s ease-in-out";
        }, 500 * index);
    });

    const menuButton = document.querySelector(".menu-button");
    if (menuButton) {
        console.log("Menu button found");
        menuButton.addEventListener("click", toggleNavbar);
    } else {
        console.log("Menu button not found");
    }
});

function toggleNavbar() {
    const navbar = document.getElementById("myNavbar");
    if (navbar) {
        console.log("Navbar found");
        if (navbar.style.display === "none" || navbar.style.display === "") {
            navbar.style.display = "block";
            console.log("Navbar displayed");
        } else {
            navbar.style.display = "none";
            console.log("Navbar hidden");
        }
    } else {
        console.log("Navbar not found");
    }
}
