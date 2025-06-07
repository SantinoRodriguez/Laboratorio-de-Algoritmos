// === Variables y Referencias ===
        const BotonMenu = document.getElementById('BotonMenu');
        const MenuColapsable = document.getElementById('MenuColapsable');
        const BotonTema = document.getElementById("Tema");
        const IconoTema = document.getElementById("IconoTema");
        const Body = document.body;
        const FormularioContacto = document.getElementById('FormularioContacto');

        // === Funcionalidad del Menú Hamburguesa ===
        BotonMenu.addEventListener('click', () => {
            if (MenuColapsable.style.display === 'flex') {
                MenuColapsable.style.display = 'none';
                BotonMenu.innerHTML = '☰';
            } else {
                MenuColapsable.style.display = 'flex';
                BotonMenu.innerHTML = '✕';
            }
        });

        // Cerrar el menú si se hace clic en un enlace
        const EnlacesMenu = MenuColapsable.querySelectorAll('a');
        EnlacesMenu.forEach((Enlace) => {
            Enlace.addEventListener('click', () => {
                MenuColapsable.style.display = 'none';
                BotonMenu.innerHTML = '☰';
            });
        });

        // Cerrar menú al hacer clic fuera de él
        document.addEventListener('click', (event) => {
            if (!MenuColapsable.contains(event.target) && !BotonMenu.contains(event.target)) {
                if (MenuColapsable.style.display === 'flex') {
                    MenuColapsable.style.display = 'none';
                    BotonMenu.innerHTML = '☰';
                }
            }
        });

        // === Funcionalidad del Cambio de Tema ===
        // Aplicar tema guardado al cargar la página
        const TemaGuardado = localStorage.getItem("tema");
        if (TemaGuardado === "claro") {
            Body.classList.add("claro");
            IconoTema.className = "fas fa-sun";
        } else {
            IconoTema.className = "fas fa-moon";
        }

        // Cambiar tema al hacer clic en el botón
        BotonTema.addEventListener("click", () => {
            Body.classList.toggle("claro");
            const TemaActual = Body.classList.contains("claro") ? "claro" : "oscuro";
            
            // Cambiar el icono según el tema
            if (TemaActual === "claro") {
                IconoTema.className = "fas fa-sun";
            } else {
                IconoTema.className = "fas fa-moon";
            }
            
            // Guardar el tema en localStorage
            localStorage.setItem("tema", TemaActual);
        });

        // === Funcionalidad del Formulario de Contacto ===
        FormularioContacto.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Obtener los valores del formulario
            const nombre = e.target.querySelector('input[type="text"]').value;
            const email = e.target.querySelector('input[type="email"]').value;
            const mensaje = e.target.querySelector('textarea').value;
            
            // Simular envío del formulario
            alert(`¡Gracias ${nombre}! Tu mensaje ha sido enviado. Te contactaré pronto a ${email}.`);
            
            // Limpiar el formulario
            e.target.reset();
        });

        // === Scroll Suave Mejorado ===
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // === Animación de Entrada para Elementos ===
        const observador = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        // Observar tarjetas de habilidades y proyectos
        document.querySelectorAll('.TarjetaHabilidad, .TarjetaProyecto').forEach(tarjeta => {
            tarjeta.style.opacity = '0';
            tarjeta.style.transform = 'translateY(30px)';
            tarjeta.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observador.observe(tarjeta);
        });

        // === Funcionalidad de Teclado ===
        document.addEventListener('keydown', (e) => {
            // Cerrar menú con Escape
            if (e.key === 'Escape' && MenuColapsable.style.display === 'flex') {
                MenuColapsable.style.display = 'none';
                BotonMenu.innerHTML = '☰';
            }
            
            // Cambiar tema con Ctrl + D
            if (e.ctrlKey && e.key === 'd') {
                e.preventDefault();
                BotonTema.click();
            }
        });

        // === Mejorar Accesibilidad ===
        // Agregar indicadores de focus visibles
        document.addEventListener('DOMContentLoaded', () => {
            const elementos = document.querySelectorAll('a, button, input, textarea');
            elementos.forEach(elemento => {
                elemento.addEventListener('focus', () => {
                    elemento.style.outline = `2px solid var(--color-primario)`;
                    elemento.style.outlineOffset = '2px';
                });
                
                elemento.addEventListener('blur', () => {
                    elemento.style.outline = 'none';
                });
            });
        });

        // === Preloader Simple ===
        window.addEventListener('load', () => {
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease';
            setTimeout(() => {
                document.body.style.opacity = '1';
            }, 100);
        });