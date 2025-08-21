// Variables globales
let hasUnsavedChanges = false;
let originalFormData = {};

// Función para inicializar el editor
function initializeEditor() {
    setupEventListeners();
    updateCounters();
    captureOriginalData();
    setupImagePreview();
    setupFormValidation();
    setupKeyboardShortcuts();
    setupDragDrop();
    
    console.log('Editor de posts inicializado correctamente');
}

// Capturar datos originales del formulario
function captureOriginalData() {
    const form = document.getElementById('formEditor');
    const formData = new FormData(form);
    
    originalFormData = {
        title: document.getElementById('id_title').value,
        text: document.getElementById('id_text').value,
        category: document.getElementById('id_category').value,
        external_link: document.getElementById('id_external_link').value,
        // Capturar tags actuales
        tags: Array.from(document.querySelectorAll('.TagItem')).map(tag => 
            tag.textContent.replace('×', '').trim()
        )
    };
}

// Configurar event listeners principales
function setupEventListeners() {
    const titleInput = document.getElementById('id_title');
    const textArea = document.getElementById('id_text');
    const form = document.getElementById('formEditor');
    
    // Event listeners para actualizar contadores y vista previa
    titleInput?.addEventListener('input', handleTitleInput);
    textArea?.addEventListener('input', handleTextInput);
    
    // Event listener para detectar cambios en el formulario
    form?.addEventListener('input', markAsChanged);
    form?.addEventListener('change', markAsChanged);
    
    // Auto-resize para textarea
    textArea?.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = Math.min(this.scrollHeight, 600) + 'px';
    });
    
    // Event listener para subida de imagen
    const imageInput = document.getElementById('id_image');
    imageInput?.addEventListener('change', handleImageUpload);
}

// Manejar entrada de título
function handleTitleInput(event) {
    const length = event.target.value.length;
    const counter = document.getElementById('contadorTitulo');
    
    if (counter) {
        counter.textContent = `${length}/200`;
        
        // Cambiar color según longitud
        if (length > 180) {
            counter.style.color = 'var(--alerta-error)';
        } else if (length > 150) {
            counter.style.color = 'var(--alerta-aviso)';
        } else {
            counter.style.color = 'var(--texto-terciario)';
        }
    }
    
    updatePreview();
}

// Manejar entrada de texto
function handleTextInput(event) {
    const text = event.target.value;
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    const counter = document.getElementById('contadorPalabras');
    
    if (counter) {
        counter.textContent = `${words} palabras`;
    }
    
    updatePreview();
}

// Actualizar vista previa en tiempo real
function updatePreview() {
    const titleInput = document.getElementById('id_title');
    const textInput = document.getElementById('id_text');
    const previewTitle = document.querySelector('.PreviewTitulo');
    const previewContent = document.querySelector('.PreviewContenido');
    
    if (previewTitle && titleInput) {
        previewTitle.textContent = titleInput.value || 'Título del post...';
    }
    
    if (previewContent && textInput) {
        const content = textInput.value || 'Contenido del post...';
        // Convertir saltos de línea a <br> y limitar a 300 caracteres para preview
        const limitedContent = content.length > 300 ? 
            content.substring(0, 300) + '...' : content;
        previewContent.innerHTML = limitedContent.replace(/\n/g, '<br>');
    }
}

// Actualizar contadores iniciales
function updateCounters() {
    const titleInput = document.getElementById('id_title');
    const textArea = document.getElementById('id_text');
    
    if (titleInput) {
        const titleLength = titleInput.value.length;
        const titleCounter = document.getElementById('contadorTitulo');
        if (titleCounter) {
            titleCounter.textContent = `${titleLength}/200`;
        }
    }
    
    if (textArea) {
        const words = textArea.value.trim() ? textArea.value.trim().split(/\s+/).length : 0;
        const wordCounter = document.getElementById('contadorPalabras');
        if (wordCounter) {
            wordCounter.textContent = `${words} palabras`;
        }
    }
    
    updatePreview();
}

// Marcar formulario como modificado
function markAsChanged() {
    hasUnsavedChanges = true;
    
    // Cambiar el badge de estado si está disponible
    const badge = document.getElementById('badgeEstado');
    if (badge && !badge.classList.contains('modificado')) {
        badge.classList.add('modificando');
        badge.innerHTML = `
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
                <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
            </svg>
            Modificando
        `;
    }
}

// Configurar previsualización de imagen
function setupImagePreview() {
    const imageInput = document.getElementById('id_image');
    if (!imageInput) return;
    
    imageInput.addEventListener('change', handleImageUpload);
}

// Manejar subida de imagen
function handleImageUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    // Validar tipo de archivo
    if (!file.type.startsWith('image/')) {
        alert('Por favor selecciona un archivo de imagen válido.');
        event.target.value = '';
        return;
    }
    
    // Validar tamaño (5MB máximo)
    const maxSize = 5 * 1024 * 1024; // 5MB en bytes
    if (file.size > maxSize) {
        alert('La imagen es demasiado grande. El tamaño máximo es 5MB.');
        event.target.value = '';
        return;
    }
    
    // Mostrar previsualización
    const reader = new FileReader();
    reader.onload = function(e) {
        const preview = document.getElementById('preview');
        const areaSubida = document.querySelector('.AreaSubida');
        const infoImagen = document.querySelector('.InfoImagen');
        
        if (preview) {
            preview.src = e.target.result;
        }
        
        if (areaSubida) {
            areaSubida.classList.add('con-imagen');
        }
        
        // Actualizar información de la imagen
        if (infoImagen) {
            const sizeKB = Math.round(file.size / 1024);
            infoImagen.innerHTML = `
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"/>
                    <path d="M12 1v6m0 6v6"/>
                </svg>
                Nueva imagen: ${file.name} (${sizeKB} KB)
            `;
        }
    };
    
    reader.readAsDataURL(file);
    markAsChanged();
}

// Aplicar formato de texto
function aplicarFormato(formato) {
    const textArea = document.getElementById('id_text');
    if (!textArea) return;
    
    const start = textArea.selectionStart;
    const end = textArea.selectionEnd;
    const selectedText = textArea.value.substring(start, end);
    
    let formattedText = '';
    let cursorOffset = 0;
    
    switch(formato) {
        case 'bold':
            formattedText = `**${selectedText}**`;
            cursorOffset = selectedText ? 0 : 2;
            break;
        case 'italic':
            formattedText = `*${selectedText}*`;
            cursorOffset = selectedText ? 0 : 1;
            break;
        case 'code':
            formattedText = `\`${selectedText}\``;
            cursorOffset = selectedText ? 0 : 1;
            break;
    }
    
    // Insertar texto formateado
    const newText = textArea.value.substring(0, start) + formattedText + textArea.value.substring(end);
    textArea.value = newText;
    
    // Posicionar cursor
    const newPosition = selectedText ? 
        start + formattedText.length : 
        start + cursorOffset;
    
    textArea.focus();
    textArea.setSelectionRange(newPosition, newPosition);
    
    // Actualizar contadores y vista previa
    handleTextInput({ target: textArea });
    markAsChanged();
}

// Gestión de tags
function agregarTag(event) {
    if (event.key !== 'Enter') return;
    
    event.preventDefault();
    const input = event.target;
    const tagName = input.value.trim();
    
    if (!tagName) return;
    
    // Verificar que no exista ya
    if (existeTag(tagName)) {
        input.value = '';
        return;
    }
    
    // Crear elemento tag
    const container = document.getElementById('tagsContainer');
    const tagElement = document.createElement('span');
    tagElement.className = 'TagItem';
    tagElement.innerHTML = `
        ${tagName}
        <button type="button" onclick="eliminarTag(this)" class="EliminarTag">×</button>
    `;
    
    container.appendChild(tagElement);
    input.value = '';
    markAsChanged();
}

function eliminarTag(button) {
    button.parentElement.remove();
    markAsChanged();
}

function existeTag(tagName) {
    const tags = document.querySelectorAll('.TagItem');
    return Array.from(tags).some(tag => 
        tag.textContent.replace('×', '').trim().toLowerCase() === tagName.toLowerCase()
    );
}

// Validación del formulario
function setupFormValidation() {
    const form = document.getElementById('formEditor');
    if (!form) return;
    
    form.addEventListener('submit', function(event) {
        if (!validateForm()) {
            event.preventDefault();
            return false;
        }
        
        // Marcar como guardado
        hasUnsavedChanges = false;
    });
}

function validateForm() {
    const title = document.getElementById('id_title')?.value.trim();
    const content = document.getElementById('id_text')?.value.trim();
    
    if (!title) {
        alert('Por favor, ingresa un título para el post.');
        document.getElementById('id_title')?.focus();
        return false;
    }
    
    if (title.length > 200) {
        alert('El título no puede exceder los 200 caracteres.');
        document.getElementById('id_title')?.focus();
        return false;
    }
    
    if (!content) {
        alert('Por favor, ingresa contenido para el post.');
        document.getElementById('id_text')?.focus();
        return false;
    }
    
    return true;
}

// Atajos de teclado
function setupKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        const activeElement = document.activeElement;
        const isTextArea = activeElement && activeElement.id === 'id_text';
        
        // Ctrl/Cmd + S para guardar
        if ((e.ctrlKey || e.metaKey) && e.key === 's') {
            e.preventDefault();
            const form = document.getElementById('formEditor');
            if (form && validateForm()) {
                // Simular clic en guardar
                const saveButton = form.querySelector('button[name="action"][value="save"]');
                if (saveButton) {
                    saveButton.click();
                }
            }
        }
        
        // Formateo solo en textarea
        if (isTextArea) {
            // Ctrl/Cmd + B para negrita
            if ((e.ctrlKey || e.metaKey) && e.key === 'b') {
                e.preventDefault();
                aplicarFormato('bold');
            }
            
            // Ctrl/Cmd + I para cursiva
            if ((e.ctrlKey || e.metaKey) && e.key === 'i') {
                e.preventDefault();
                aplicarFormato('italic');
            }
            
            // Ctrl/Cmd + ` para código
            if ((e.ctrlKey || e.metaKey) && e.key === '`') {
                e.preventDefault();
                aplicarFormato('code');
            }
        }
    });
}

// Drag and drop para imágenes
function setupDragDrop() {
    const areaSubida = document.querySelector('.AreaSubida');
    if (!areaSubida) return;
    
    // Prevenir comportamiento por defecto
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        areaSubida.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    // Efectos visuales
    ['dragenter', 'dragover'].forEach(eventName => {
        areaSubida.addEventListener(eventName, highlight, false);
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
        areaSubida.addEventListener(eventName, unhighlight, false);
    });
    
    function highlight() {
        areaSubida.style.borderColor = 'var(--acento-medio)';
        areaSubida.style.backgroundColor = 'rgba(77, 171, 247, 0.1)';
        areaSubida.style.transform = 'scale(1.02)';
    }
    
    function unhighlight() {
        areaSubida.style.borderColor = '';
        areaSubida.style.backgroundColor = '';
        areaSubida.style.transform = '';
    }
    
    // Manejar drop
    areaSubida.addEventListener('drop', function(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length > 0) {
            const file = files[0];
            if (file.type.startsWith('image/')) {
                const imageInput = document.getElementById('id_image');
                if (imageInput) {
                    // Crear un nuevo FileList
                    const dataTransfer = new DataTransfer();
                    dataTransfer.items.add(file);
                    imageInput.files = dataTransfer.files;
                    
                    // Disparar evento change
                    imageInput.dispatchEvent(new Event('change', { bubbles: true }));
                }
            } else {
                alert('Por favor, arrastra solo archivos de imagen.');
            }
        }
    }, false);
}

// Confirmar eliminación
function confirmarEliminacion() {
    const confirmMessage = '¿Estás seguro de que quieres eliminar este post?\n\nEsta acción no se puede deshacer.';
    
    if (confirm(confirmMessage)) {
        // El formulario de eliminación se enviará normalmente
        return true;
    }
    return false;
}

// Prevenir pérdida de cambios
function setupBeforeUnload() {
    window.addEventListener('beforeunload', function(e) {
        if (hasUnsavedChanges) {
            e.preventDefault();
            e.returnValue = '¿Estás seguro de que quieres salir? Tienes cambios sin guardar.';
            return e.returnValue;
        }
    });
}

// Auto-guardado (opcional, comentado para no interferir con Django)
/*
function setupAutoSave() {
    let autoSaveTimeout;
    
    function scheduleAutoSave() {
        clearTimeout(autoSaveTimeout);
        autoSaveTimeout = setTimeout(performAutoSave, 30000); // 30 segundos
    }
    
    function performAutoSave() {
        if (hasUnsavedChanges && validateForm()) {
            const formData = new FormData(document.getElementById('formEditor'));
            
            fetch(window.location.href, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => {
                if (response.ok) {
                    hasUnsavedChanges = false;
                    showNotification('Auto-guardado completado', 'success');
                }
            })
            .catch(error => {
                console.error('Error en auto-guardado:', error);
            });
        }
    }
    
    // Programar auto-guardado cuando hay cambios
    document.getElementById('formEditor').addEventListener('input', scheduleAutoSave);
}
*/

// Función de inicialización principal
function init() {
    // Esperar a que el DOM esté completamente cargado
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeEditor);
    } else {
        initializeEditor();
    }
    
    setupBeforeUnload();
    // setupAutoSave(); // Descomenta si quieres auto-guardado
}

// Inicializar
init();