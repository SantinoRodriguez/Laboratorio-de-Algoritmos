// Obtener referencias
const BotonMenu = document.getElementById('BotonMenu');
const MenuColapsable = document.getElementById('MenuColapsable');

// Evento para mostrar u ocultar el menú
BotonMenu.addEventListener('click', () => {
    // Alternar visibilidad usando clases
    if (MenuColapsable.style.display === 'flex') {
        MenuColapsable.style.display = 'none';
    } else {
        MenuColapsable.style.display = 'flex';
    }
});

// Cerrar el menú si se hace clic en un enlace
const EnlacesMenu = MenuColapsable.querySelectorAll('a');
EnlacesMenu.forEach((Enlace) => {
    Enlace.addEventListener('click', () => {
        MenuColapsable.style.display = 'none';
    });
});


const BotonTema = document.getElementById("Tema");
const Body = document.body;

// Al cargar, aplicar tema guardado
if (localStorage.getItem("tema") === "claro") {
    Body.classList.add("claro");
    BotonTema.textContent = "🌙";
}

BotonTema.addEventListener("click", () => {
    Body.classList.toggle("claro");
    const TemaActual = Body.classList.contains("claro") ? "claro" : "oscuro";
    BotonTema.textContent = TemaActual === "claro" ? "🌙" : "☀️";
    localStorage.setItem("tema", TemaActual);
});


