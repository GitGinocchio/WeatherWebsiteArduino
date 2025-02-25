document.addEventListener("DOMContentLoaded", function() {
    const formElements = document.querySelectorAll("form label, form input, form button");

    formElements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = 1;
            el.style.transition = "opacity 1s ease-in-out";
        }, 500 * index);
    });
});
