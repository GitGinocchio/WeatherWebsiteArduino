// Ho dovuto modificare questo script pero' per favore non fate commit di cose che non funzionano
// Una commit va fatta se tutto quello che avete fatto fino a quel punto funziona altrimenti non fatela
// Altrimenti le vostre modifiche potrebbero creare confusione
//
// - Giulio

document.addEventListener("DOMContentLoaded", function() {
    const registerForm = document.getElementById("register-form");

    registerForm.addEventListener("submit", function(event) {
        event.preventDefault();
        
        // const email = registerForm.querySelector('input[type="email"]').value;
        // const username = registerForm.querySelector('input[type="text"]').value;
        const password = registerForm.querySelector('input[type="password"]').value;
        const repeatPassword = registerForm.querySelector('input[placeholder="Repeat Password"]').value;

        if (password !== repeatPassword) {
            console.error("Passwords do not match");
            alert("Le password non coincidono. Riprova.");
            return;
        }
        
        
        event.target.submit();
    });
});