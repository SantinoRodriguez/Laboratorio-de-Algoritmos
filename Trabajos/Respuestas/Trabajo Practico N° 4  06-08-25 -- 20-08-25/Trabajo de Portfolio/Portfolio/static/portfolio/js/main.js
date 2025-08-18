const CONFIG = {
    scrollThreshold: 50,
    animationDuration: 300,
    loaderDelay: 1500, // Reducido para testing
    counterSpeed: 50,
    textRotateSpeed: 2000,
    progressUpdateInterval: 100,
    debounceDelay: 250,
    intersectionThreshold: 0.2
};

const SELECTORS = {
    loader: '#cargador',
    header: '#cabecera',
    menu: '#menu',
    menuToggle: '#menuToggle',
    themeToggle: '#cambiarTema',
    scrollTop: '#botonSubir',
    progressBar: '#barraProgreso',
    contactForm: '#contactForm',
    textRotate: '#textoRotativo',
    navLinks: '.Enlaces .Enlace',
    filterButtons: '.Filtro',
    projects: '.Proyecto',
    counters: '.Numero',
    skillBars: '.Progreso'
};

// ==============================================
// UTILIDADES
// ==============================================

// Theme toggle
const themeToggle = document.getElementById('cambiarTema');
const body = document.body;

// Get saved theme or default to light
const savedTheme = localStorage.getItem('theme') || 'light';
body.setAttribute('data-theme', savedTheme);

themeToggle.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
});

// Search functionality
const searchInput = document.getElementById('busquedaInput');
searchInput.addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    // Implement search logic here
    console.log('Searching for:', searchTerm);
});

// Filter functionality
const filters = document.querySelectorAll('.FiltroPost');
filters.forEach(filter => {
    filter.addEventListener('click', () => {
        // Remove active class from all filters
        filters.forEach(f => f.classList.remove('activo'));
        // Add active class to clicked filter
        filter.classList.add('activo');
        
        // Implement filter logic here
        console.log('Filter selected:', filter.textContent);
    });
});

// Post actions
document.addEventListener('click', (e) => {
    if (e.target.closest('.BotonAccion.like')) {
        const button = e.target.closest('.BotonAccion.like');
        button.classList.toggle('activo');
        
        // Update counter
        const counter = button.querySelector('span');
        if (counter) {
            let count = parseInt(counter.textContent);
            counter.textContent = button.classList.contains('activo') ? count + 1 : count - 1;
        }
    }
    
    if (e.target.closest('.BotonAccion.bookmark')) {
        const button = e.target.closest('.BotonAccion.bookmark');
        button.classList.toggle('activo');
    }
});

// Mobile menu toggle
const menuToggle = document.getElementById('menuToggle');
const menuLateral = document.getElementById('menuLateral');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        menuLateral.classList.toggle('activo');
    });
}

// Responsive adjustments
function handleResize() {
    if (window.innerWidth <= 768) {
        document.getElementById('menuToggle').style.display = 'flex';
    } else {
        document.getElementById('menuToggle').style.display = 'none';
        menuLateral.classList.remove('activo');
    }
}

window.addEventListener('resize', handleResize);
handleResize(); // Call on load

// Infinite scroll simulation
let isLoading = false;
const loadingSkeleton = document.getElementById('loadingSkeleton');

function showLoading() {
    if (isLoading) return;
    isLoading = true;
    loadingSkeleton.style.display = 'block';
    
    // Simulate API call
    setTimeout(() => {
        loadingSkeleton.style.display = 'none';
        isLoading = false;
        // Here you would append new posts
    }, 2000);
}

// Trigger loading on scroll near bottom
window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 1000) {
        showLoading();
    }
});

// Sidebar menu interactions
const sidebarItems = document.querySelectorAll('.MenuLateral .Bloques li');
sidebarItems.forEach(item => {
    item.addEventListener('click', () => {
        // Remove active class from all items
        sidebarItems.forEach(i => i.classList.remove('activo'));
        // Add active class to clicked item
        item.classList.add('activo');
    });
});

// Export ES6 (si se usa en módulos)
export default Portfolio;
