function validate() {
    var pass1 = document.forms["tarea2"]["password1"].value;
    var pass2 = document.forms["tarea2"]["password1"].value;
    if (pass1 != pass2) {
        alert("Las contraseñas no osn las mismas!");
        return false;
    }
}