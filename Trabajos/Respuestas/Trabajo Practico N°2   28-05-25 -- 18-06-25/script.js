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
