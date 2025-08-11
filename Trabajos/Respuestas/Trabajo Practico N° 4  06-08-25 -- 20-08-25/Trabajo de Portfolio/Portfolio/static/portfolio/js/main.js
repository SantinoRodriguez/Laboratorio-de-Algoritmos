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

const Utils = {
    // Función de debounce para optimizar eventos
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    // Throttle para eventos de scroll
    throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },

    // Animación suave de scroll
    smoothScroll(target, duration = 800) {
        const targetElement = document.querySelector(target);
        if (!targetElement) return;

        const targetPosition = targetElement.offsetTop - 80;
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        let startTime = null;

        function animation(currentTime) {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = Utils.easeInOutQuad(timeElapsed, startPosition, distance, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(animation);
        }

        requestAnimationFrame(animation);
    },

    // Función de easing para animaciones
    easeInOutQuad(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    },

    // Obtener posición de scroll
    getScrollPercent() {
        const h = document.documentElement;
        const b = document.body;
        const st = 'scrollTop';
        const sh = 'scrollHeight';
        return (h[st] || b[st]) / ((h[sh] || b[sh]) - h.clientHeight) * 100;
    },

    // Formatear números
    formatNumber(num) {
        return new Intl.NumberFormat().format(num);
    },

    // Validar email
    isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
};

// ==============================================
// CLASE PRINCIPAL DEL PORTFOLIO
// ==============================================

class Portfolio {
    constructor() {
        this.isMenuOpen = false;
        this.currentTheme = localStorage.getItem('theme') || 'light';
        this.activeSection = 'inicio';
        this.projects = [];
        this.currentFilter = 'todos';
        this.observers = new Map();
        this.textRotateIndex = 0;
        this.textRotateWords = ['Full Stack', 'Frontend', 'Backend', 'Web Developer'];
        
        // Bind methods
        this.handleScroll = this.handleScroll.bind(this);
        this.handleResize = this.handleResize.bind(this);
        
        console.log('🎯 Inicializando Portfolio...');
        this.init();
    }

    // Inicialización principal
    init() {
        try {
            console.log('🚀 Configurando Portfolio...');
            
            this.initializeTheme();
            this.setupEventListeners();
            this.handleLoader();
            this.initializeAnimations();
            this.startTextRotation();
            this.initializeProjects();
            this.preloadImages();
            
            console.log('✅ Portfolio inicializado correctamente');
        } catch (error) {
            console.error('❌ Error inicializando Portfolio:', error);
        }
    }

    // ==============================================
    // EVENT LISTENERS
    // ==============================================

    setupEventListeners() {
        console.log('📡 Configurando event listeners...');
        
        // DOM Content Loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.onDOMReady());
        } else {
            this.onDOMReady();
        }

        // Navegación
        this.setupNavigationListeners();
        
        // Scroll events
        this.setupScrollListeners();
        
        // Theme toggle
        this.setupThemeListener();
        
        // Menu toggle
        this.setupMenuListener();
        
        // Form handling
        this.setupFormListener();
        
        // Filter buttons
        this.setupFilterListeners();
        
        // Resize handling
        window.addEventListener('resize', Utils.debounce(() => {
            this.handleResize();
        }, CONFIG.debounceDelay));

        // Keyboard navigation
        document.addEventListener('keydown', (e) => this.handleKeyboard(e));
    }

    onDOMReady() {
        console.log('✅ DOM ready, inicializando componentes...');
        this.initializeCounters();
        this.initializeSkillBars();
        this.updateActiveNavLink();
        this.initializeIntersectionObservers();
    }

    setupNavigationListeners() {
        const navLinks = document.querySelectorAll(SELECTORS.navLinks);
        console.log(`🔗 Configurando ${navLinks.length} enlaces de navegación`);
        
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const target = link.getAttribute('href');
                if (target && target.startsWith('#')) {
                    Utils.smoothScroll(target);
                    this.closeMenu();
                    this.updateActiveNavLink(target.substring(1));
                }
            });
        });

        // Logo click
        const logo = document.querySelector('.Logo');
        if (logo) {
            logo.addEventListener('click', (e) => {
                e.preventDefault();
                Utils.smoothScroll('#inicio');
            });
        }
    }

    setupScrollListeners() {
        const throttledScroll = Utils.throttle(() => {
            this.handleScroll();
        }, 16); // 60fps

        window.addEventListener('scroll', throttledScroll);
    }

    setupThemeListener() {
        const themeToggle = document.querySelector(SELECTORS.themeToggle);
        if (themeToggle) {
            themeToggle.addEventListener('click', () => this.toggleTheme());
            console.log('🎨 Theme toggle configurado');
        }
    }

    setupMenuListener() {
        const menuToggle = document.querySelector(SELECTORS.menuToggle);
        if (menuToggle) {
            menuToggle.addEventListener('click', () => this.toggleMenu());
            console.log('🍔 Menu toggle configurado');
        }

        // Cerrar menu al hacer click fuera
        document.addEventListener('click', (e) => {
            const menu = document.querySelector(SELECTORS.menu);
            const menuToggle = document.querySelector(SELECTORS.menuToggle);
            
            if (this.isMenuOpen && menu && menuToggle &&
                !menu.contains(e.target) && 
                !menuToggle.contains(e.target)) {
                this.closeMenu();
            }
        });
    }

    setupFormListener() {
        const form = document.querySelector(SELECTORS.contactForm);
        if (form) {
            form.addEventListener('submit', (e) => this.handleFormSubmit(e));
            console.log('📧 Formulario de contacto configurado');
        }
    }

    setupFilterListeners() {
        const filterButtons = document.querySelectorAll(SELECTORS.filterButtons);
        console.log(`🔍 Configurando ${filterButtons.length} filtros de proyecto`);
        
        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                const filter = button.getAttribute('data-filter');
                this.filterProjects(filter);
                this.updateActiveFilter(button);
            });
        });
    }

    // ==============================================
    // MANEJO DE SCROLL
    // ==============================================

    handleScroll() {
        const scrollY = window.pageYOffset;
        
        // Header behavior
        this.updateHeader(scrollY);
        
        // Progress bar
        this.updateProgressBar();
        
        // Scroll to top button
        this.updateScrollTopButton(scrollY);
        
        // Active navigation
        this.updateActiveNavLink();
        
        // Parallax effects
        this.handleParallax(scrollY);
    }

    updateHeader(scrollY) {
        const header = document.querySelector(SELECTORS.header);
        if (!header) return;

        if (scrollY > CONFIG.scrollThreshold) {
            header.style.background = 'rgba(255, 255, 255, 0.98)';
            header.style.backdropFilter = 'blur(20px)';
            header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
        } else {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
            header.style.boxShadow = 'none';
        }
    }

    updateProgressBar() {
        const progressBar = document.querySelector(SELECTORS.progressBar);
        if (!progressBar) return;

        const scrollPercent = Utils.getScrollPercent();
        progressBar.style.width = `${scrollPercent}%`;
    }

    updateScrollTopButton(scrollY) {
        const scrollTopBtn = document.querySelector(SELECTORS.scrollTop);
        if (!scrollTopBtn) return;

        if (scrollY > 500) {
            scrollTopBtn.classList.add('visible');
            scrollTopBtn.onclick = () => Utils.smoothScroll('#inicio');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    }

    updateActiveNavLink(activeSection = null) {
        if (activeSection) {
            this.activeSection = activeSection;
        } else {
            // Determinar sección activa basada en scroll
            const sections = ['inicio', 'sobre', 'habilidades', 'proyectos', 'experiencia', 'contacto'];
            const scrollY = window.pageYOffset + 100;

            for (let section of sections) {
                const element = document.getElementById(section);
                if (element && scrollY >= element.offsetTop && scrollY < element.offsetTop + element.offsetHeight) {
                    this.activeSection = section;
                    break;
                }
            }
        }

        // Actualizar enlaces activos
        const navLinks = document.querySelectorAll(SELECTORS.navLinks);
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href && href.substring(1) === this.activeSection) {
                link.classList.add('activo');
            } else {
                link.classList.remove('activo');
            }
        });
    }

    handleParallax(scrollY) {
        // Elementos flotantes
        const floatingElements = document.querySelectorAll('.Flotante');
        floatingElements.forEach((element, index) => {
            const speed = 0.3 + (index * 0.1);
            element.style.transform = `translateY(${scrollY * speed}px)`;
        });

        // Hero background
        const hero = document.querySelector('.Bienvenida');
        if (hero) {
            hero.style.transform = `translateY(${scrollY * 0.5}px)`;
        }
    }

    // ==============================================
    // NAVEGACIÓN Y MENÚ
    // ==============================================

    toggleMenu() {
        this.isMenuOpen = !this.isMenuOpen;
        const menu = document.querySelector(SELECTORS.menu);
        const menuToggle = document.querySelector(SELECTORS.menuToggle);
        
        if (menu && menuToggle) {
            menu.classList.toggle('activo', this.isMenuOpen);
            menuToggle.classList.toggle('activo', this.isMenuOpen);
            
            // Prevenir scroll del body cuando el menú está abierto
            document.body.classList.toggle('no-scroll', this.isMenuOpen);
        }
    }

    closeMenu() {
        this.isMenuOpen = false;
        const menu = document.querySelector(SELECTORS.menu);
        const menuToggle = document.querySelector(SELECTORS.menuToggle);
        
        if (menu && menuToggle) {
            menu.classList.remove('activo');
            menuToggle.classList.remove('activo');
            document.body.classList.remove('no-scroll');
        }
    }

    // ==============================================
    // TEMA OSCURO/CLARO
    // ==============================================

    initializeTheme() {
        console.log(`🎨 Inicializando tema: ${this.currentTheme}`);
        document.documentElement.setAttribute('data-theme', this.currentTheme);
        this.updateThemeIcon();
    }

    toggleTheme() {
        this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', this.currentTheme);
        localStorage.setItem('theme', this.currentTheme);
        this.updateThemeIcon();
        
        // Animate theme change
        document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
        setTimeout(() => {
            document.body.style.transition = '';
        }, 300);
    }

    updateThemeIcon() {
        const themeBtn = document.querySelector(SELECTORS.themeToggle);
        if (themeBtn) {
            const sunIcon = themeBtn.querySelector('.sol');
            const moonIcon = themeBtn.querySelector('.luna');
            
            if (sunIcon && moonIcon) {
                if (this.currentTheme === 'dark') {
                    sunIcon.style.display = 'none';
                    moonIcon.style.display = 'block';
                } else {
                    sunIcon.style.display = 'block';
                    moonIcon.style.display = 'none';
                }
            }
        }
    }

    // ==============================================
    // LOADER Y ANIMACIONES INICIALES
    // ==============================================

    handleLoader() {
        console.log('⏳ Iniciando loader...');
        const loader = document.querySelector(SELECTORS.loader);
        if (!loader) {
            console.warn('⚠️ Loader no encontrado');
            this.startInitialAnimations();
            return;
        }

        // Simular carga
        setTimeout(() => {
            console.log('✅ Ocultando loader...');
            loader.classList.add('oculto');
            this.startInitialAnimations();
            
            // Remover loader del DOM después de la animación
            setTimeout(() => {
                if (loader.parentNode) {
                    loader.parentNode.removeChild(loader);
                    console.log('🗑️ Loader removido del DOM');
                }
            }, 500);
        }, CONFIG.loaderDelay);
    }

    startInitialAnimations() {
        console.log('🎬 Iniciando animaciones...');
        
        // Animar elementos del hero
        const heroElements = document.querySelectorAll('.Texto > *');
        heroElements.forEach((element, index) => {
            setTimeout(() => {
                element.classList.add('fade-in-up');
            }, index * 100);
        });

        // Animar foto
        const photo = document.querySelector('.Marco');
        if (photo) {
            setTimeout(() => {
                photo.classList.add('fade-in-right');
            }, 200);
        }
    }

    initializeAnimations() {
        // Configurar animaciones CSS iniciales
        const animatedElements = document.querySelectorAll('[class*="fade-"]');
        animatedElements.forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
        });
    }

    // ==============================================
    // INTERSECTION OBSERVERS
    // ==============================================

    initializeIntersectionObservers() {
        console.log('👁️ Configurando intersection observers...');
        
        const options = {
            threshold: CONFIG.intersectionThreshold,
            rootMargin: '-50px'
        };

        // Observer para animaciones de entrada
        const animationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, options);

        // Observer para contadores
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, options);

        // Observer para barras de progreso
        const progressObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateSkillBar(entry.target);
                    progressObserver.unobserve(entry.target);
                }
            });
        }, options);

        // Aplicar observers
        this.applyObservers(animationObserver, counterObserver, progressObserver);
    }

    applyObservers(animationObserver, counterObserver, progressObserver) {
        // Elementos animables
        const animatableElements = document.querySelectorAll(
            '.Categoria, .Proyecto, .EventoContenido, .Caracteristica, .InfoCard'
        );
        animatableElements.forEach(el => animationObserver.observe(el));

        // Contadores
        const counters = document.querySelectorAll(SELECTORS.counters);
        counters.forEach(counter => counterObserver.observe(counter));

        // Barras de progreso
        const skillBars = document.querySelectorAll(SELECTORS.skillBars);
        skillBars.forEach(bar => {
            const parent = bar.parentElement;
            if (parent) progressObserver.observe(parent);
        });
    }

    // ==============================================
    // CONTADORES ANIMADOS
    // ==============================================

    initializeCounters() {
        const counters = document.querySelectorAll(SELECTORS.counters);
        console.log(`🔢 Inicializando ${counters.length} contadores`);
        counters.forEach(counter => {
            counter.textContent = '0';
        });
    }

    animateCounter(counter) {
        const target = parseInt(counter.getAttribute('data-target') || counter.textContent);
        const increment = target / (2000 / CONFIG.counterSpeed);
        let current = 0;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                counter.textContent = target;
                clearInterval(timer);
            } else {
                counter.textContent = Math.floor(current);
            }
        }, CONFIG.counterSpeed);
    }

    // ==============================================
    // BARRAS DE HABILIDADES
    // ==============================================

    initializeSkillBars() {
        const skillBars = document.querySelectorAll(SELECTORS.skillBars);
        console.log(`📊 Inicializando ${skillBars.length} barras de progreso`);
        skillBars.forEach(bar => {
            bar.style.width = '0%';
        });
    }

    animateSkillBar(skillContainer) {
        const progressBar = skillContainer.querySelector('.Progreso');
        if (!progressBar) return;

        const targetWidth = progressBar.getAttribute('data-width') || '80%';
        
        // Reset width
        progressBar.style.width = '0%';
        
        // Animate to target
        setTimeout(() => {
            progressBar.style.transition = 'width 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            progressBar.style.width = targetWidth;
        }, 200);
    }

    // ==============================================
    // TEXTO ROTATIVO
    // ==============================================

    startTextRotation() {
        const textElement = document.querySelector(SELECTORS.textRotate);
        if (!textElement) {
            console.log('⚠️ Elemento de texto rotativo no encontrado');
            return;
        }

        console.log('🔄 Iniciando rotación de texto');
        
        setInterval(() => {
            this.textRotateIndex = (this.textRotateIndex + 1) % this.textRotateWords.length;
            
            // Fade out
            textElement.style.opacity = '0';
            textElement.style.transform = 'translateY(10px)';
            
            setTimeout(() => {
                textElement.textContent = this.textRotateWords[this.textRotateIndex];
                textElement.style.opacity = '1';
                textElement.style.transform = 'translateY(0)';
            }, 200);
        }, CONFIG.textRotateSpeed);
    }

    // ==============================================
    // FILTRO DE PROYECTOS
    // ==============================================

    initializeProjects() {
        const projects = document.querySelectorAll(SELECTORS.projects);
        console.log(`📁 Inicializando ${projects.length} proyectos`);
        
        this.projects = Array.from(projects).map(project => ({
            element: project,
            category: project.getAttribute('data-categoria') || 'web'
        }));
    }

    filterProjects(filter) {
        if (filter === this.currentFilter) return;
        
        console.log(`🔍 Filtrando proyectos: ${filter}`);
        this.currentFilter = filter;
        
        this.projects.forEach(({ element, category }, index) => {
            const shouldShow = filter === 'todos' || category === filter;
            
            setTimeout(() => {
                if (shouldShow) {
                    element.classList.remove('oculto');
                } else {
                    element.classList.add('oculto');
                }
            }, index * 50);
        });
    }

    updateActiveFilter(activeButton) {
        const filterButtons = document.querySelectorAll(SELECTORS.filterButtons);
        filterButtons.forEach(button => button.classList.remove('activo'));
        activeButton.classList.add('activo');
    }

    // ==============================================
    // FORMULARIO DE CONTACTO
    // ==============================================

    handleFormSubmit(e) {
        e.preventDefault();
        console.log('📧 Procesando formulario...');
        
        const form = e.target;
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        
        // Validación
        if (!this.validateForm(data)) return;
        
        // Simular envío
        this.submitForm(data, form);
    }

    validateForm(data) {
        const { nombre, email, asunto, mensaje } = data;
        
        if (!nombre || !nombre.trim() || !email || !email.trim() || 
            !asunto || !asunto.trim() || !mensaje || !mensaje.trim()) {
            this.showFormMessage('Por favor, completa todos los campos requeridos.', 'error');
            return false;
        }
        
        if (!Utils.isValidEmail(email)) {
            this.showFormMessage('Por favor, introduce un email válido.', 'error');
            return false;
        }
        
        if (mensaje.trim().length < 10) {
            this.showFormMessage('El mensaje debe tener al menos 10 caracteres.', 'error');
            return false;
        }
        
        return true;
    }

    async submitForm(data, form) {
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn ? submitBtn.innerHTML : '';
        
        // Loading state
        if (submitBtn) {
            submitBtn.innerHTML = '<span>Enviando...</span>';
            submitBtn.disabled = true;
        }
        
        try {
            // Simular envío (aquí integrarías con tu backend)
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            this.showFormMessage('¡Mensaje enviado correctamente! Te responderé pronto.', 'success');
            form.reset();
            
        } catch (error) {
            this.showFormMessage('Error al enviar el mensaje. Intenta nuevamente.', 'error');
        } finally {
            if (submitBtn) {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }
        }
    }

    showFormMessage(message, type) {
        // Crear elemento de notificación
        const notification = document.createElement('div');
        notification.className = `Notificacion ${type}`;
        notification.innerHTML = `
            <div class="NotificacionContenido">
                <span>${message}</span>
                <button class="NotificacionCerrar">&times;</button>
            </div>
        `;
        
        // Estilos dinámicos
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#40c057' : '#fa5252'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 10000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        `;
        
        document.body.appendChild(notification);
        
        // Animar entrada
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);
        
        // Auto remove
        setTimeout(() => {
            this.removeNotification(notification);
        }, 5000);
        
        // Manual close
        const closeBtn = notification.querySelector('.NotificacionCerrar');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => this.removeNotification(notification));
        }
    }

    removeNotification(notification) {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }

    // ==============================================
    // NAVEGACIÓN POR TECLADO
    // ==============================================

    handleKeyboard(e) {
        // ESC para cerrar menú
        if (e.key === 'Escape' && this.isMenuOpen) {
            this.closeMenu();
        }
        
        // Navegación con flechas en proyectos
        if (e.target.closest('.Proyecto')) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const link = e.target.querySelector('a[target="_blank"]');
                if (link) link.click();
            }
        }
    }

    // ==============================================
    // RESPONSIVE Y RESIZE
    // ==============================================

    handleResize() {
        // Cerrar menú en desktop
        if (window.innerWidth > 992 && this.isMenuOpen) {
            this.closeMenu();
        }
        
        // Recalcular posiciones para animaciones
        this.updateActiveNavLink();
        
        // Actualizar parallax
        this.handleParallax(window.pageYOffset);
    }

    // ==============================================
    // PRELOADER DE IMÁGENES
    // ==============================================

    preloadImages() {
        const images = document.querySelectorAll('img[loading="lazy"]');
        if (images.length === 0) {
            console.log('📸 No hay imágenes lazy para precargar');
            return;
        }
        
        console.log(`📸 Precargando ${images.length} imágenes`);
        
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.src;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }

    // ==============================================
    // MÉTODOS PÚBLICOS PARA DEBUGGING
    // ==============================================

    getState() {
        return {
            isMenuOpen: this.isMenuOpen,
            currentTheme: this.currentTheme,
            activeSection: this.activeSection,
            currentFilter: this.currentFilter,
            textRotateIndex: this.textRotateIndex
        };
    }

    destroy() {
        // Cleanup para testing o hot reloading
        this.observers.forEach(observer => observer.disconnect());
        window.removeEventListener('scroll', this.handleScroll);
        window.removeEventListener('resize', this.handleResize);
    }
}

// ==============================================
// INICIALIZACIÓN GLOBAL
// ==============================================

let portfolioInstance = null;

function initPortfolio() {
    if (!portfolioInstance) {
        console.log('🎯 Iniciando Portfolio...');
        portfolioInstance = new Portfolio();
        window.Portfolio = portfolioInstance; // Para debugging
        console.log('🎉 Portfolio de Santino Rodriguez listo!');
    }
}

// Auto-inicialización
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPortfolio);
} else {
    initPortfolio();
}

// Manejo de errores globales
window.addEventListener('error', (e) => {
    console.error('❌ Error global:', e.error);
});

// Hot reload para desarrollo (opcional)
if (module?.hot) {
    module.hot.accept();
    module.hot.dispose(() => {
        if (portfolioInstance?.destroy) {
            portfolioInstance.destroy();
        }
        portfolioInstance = null;
    });
}

// Export ES6 (si se usa en módulos)
export default Portfolio;
