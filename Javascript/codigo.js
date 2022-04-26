//inputs
const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const nomusuario = document.getElementById("nomusuario");
const email = document.getElementById("email");
const pass = document.getElementById("password");
const pass2 = document.getElementById("password2");
const form = document.getElementById("form");
const parrafo = document.getElementById("warnings");
const f = document.querySelector("form");
//Querys selector
nombre.placeholder = "Ingresa tu nombre";
apellido.placeholder = "Ingresa tu apellido";
nomusuario.placeholder = "Ingresa un nombre de usuario";
email.placeholder = "Escribe tu correo electronico";
password.placeholder = "Ingresa una contraseña";
password2.placeholder = "Introduce de nuevo contrase"

// Metodo para comprobar si tiene letra mayuscula o no
var letras_mayusculas="ABCDEFGHYJKLMNÑOPQRSTUVWXYZ";
function tiene_mayus(texto) {
    for (let i = 0; i < texto.length; i++) {
        if (letras_mayusculas.indexOf(texto.charAt(i), 0) != -1) {
            return 1;
        }
    }
    return 0;
}

// Metodo para que tenga minimo 6 caracteres en el nombre de usuario
 form.addEventListener("submit", e => {
     e.preventDefault();
     let warnings = "";
     let regexemail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
     let entrar = false;
     parrafo.innerHTML = "";
     if (nomusuario.value.length < 6) {
         warnings += `El nombre no es valido, necesitas 6 caracteres. <br>`
         entrar = true
     }

     if (!regexemail.test(email.value)) {
         warnings += `El email no es valido. <br>`
         entrar = true
     }

     if (tiene_mayus(pass.value) != 0) { // Validacion para mayusculas en password
        
    } else {
        warnings += `Necesitas ponerle minimo una letra mayuscula a tu contraseña. <br>`
        entrar = true
    }
    
    if (pass2.value == pass.value) { // validacion para confirmar passwords
        
    } else {
        warnings += `Las contraseñas no son iguales. <br>`
        entrar = true
    }

    if (pass.value.length < 8) {
        warnings += `La contraseña debe tener 8 caracteres. <br>`
        entrar = true
    }

    if (entrar == true) {
        parrafo.innerHTML = warnings;
        f.style.height = "625px";
    } else {
        parrafo.innerHTML = "Enviado";
        f.style.height = "510px";
        
    }
 });





