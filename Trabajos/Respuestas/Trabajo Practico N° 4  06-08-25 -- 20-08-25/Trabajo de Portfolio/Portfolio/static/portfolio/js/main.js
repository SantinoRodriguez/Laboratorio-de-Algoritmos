// Theme toggle
document.getElementById('themeToggle')?.addEventListener('click', function() {
    // Implementar toggle de tema si es necesario
    console.log('Theme toggle clicked');
});

// Search functionality
document.getElementById('searchInput')?.addEventListener('input', function(e) {
    // Implementar búsqueda si es necesario
    console.log('Search:', e.target.value);
});

// Post interactions
document.addEventListener('click', function(e) {
    if (e.target.closest('.BotonAccion')) {
        const button = e.target.closest('.BotonAccion');
        // Implementar acciones de like, bookmark, etc.
        if (button.classList.contains('like')) {
            button.classList.toggle('activo');
        } else if (button.classList.contains('bookmark')) {
            button.classList.toggle('activo');
        }
    }
});

// Export ES6 (si se usa en módulos)
export default Portfolio;
