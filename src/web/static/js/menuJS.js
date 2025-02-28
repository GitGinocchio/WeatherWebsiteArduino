document.addEventListener("DOMContentLoaded", function() {
    const formElements = document.querySelectorAll("form label, form input, form button, menu, section, nav");

    formElements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = 1;
            el.style.transition = "opacity 1s ease-in-out";
        }, 500 * index);
    });

    const arrows = document.querySelectorAll(".arrow");
    arrows.forEach(arrow => {
        arrow.addEventListener("click", function() {
            const parentUl = this.parentElement;
            parentUl.classList.toggle("open");
            this.textContent = parentUl.classList.contains("open") ? "►" : "▶";
        });
    });
});