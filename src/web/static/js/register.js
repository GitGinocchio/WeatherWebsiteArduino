document.addEventListener("DOMContentLoaded", function() {
    const registerForm = document.getElementById("register-form");

    registerForm.addEventListener("submit", function(event) {
        event.preventDefault(); 
        
        const email = registerForm.querySelector('input[type="email"]').value;
        const username = registerForm.querySelector('input[type="text"]').value;
        const password = registerForm.querySelector('input[type="password"]').value;
        const repeatPassword = registerForm.querySelector('input[placeholder="Repeat Password"]').value;

        if (password === repeatPassword) {
            console.log("Form submitted successfully with:", { email, username, password, repeatPassword });
            window.location.href = "main.html";
        } else {
            console.error("Passwords do not match");
            alert("Le password non coincidono. Riprova.");
        }
    });
});