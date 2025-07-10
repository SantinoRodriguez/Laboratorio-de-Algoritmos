# Proyecto Django - Tutorial 1

Este proyecto es una aplicación web desarrollada en **Python** utilizando el **framework Django**, como parte del trabajo práctico de la **PIA** de la materia *Laboratorio de Algoritmos* (4° año). Está basado en el primer tutorial oficial de Django y permite crear y administrar encuestas simples.

---

## Contenidos del proyecto

El proyecto incluye:

- Una app llamada polls con modelos, vistas y URLs propias.
- Templates personalizados con HTML y CSS.
- Recursos estáticos como imágenes y estilos.
- Configuración del panel de administración.
- Integración con el sistema de superusuario de Django.

---

## Estructura del repositorio

```
djangotutorial/
│   manage.py
│
├───mysite/
│   │   __init__.py
│   │   settings.py
│   │   urls.py
│   │   asgi.py
│   │   wsgi.py
│
├───polls/
│   │   __init__.py
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │
│   ├───migrations/
│   │   │   __init__.py
│   │   │   0001_initial.py
│   │
│   ├───static/
│   │   └───polls/
│   │       ├───images/
│   │       │   └───background.png
│   │       └───style.css
│   │
│   └───templates/
│       └───polls/
│           ├───detail.html
│           ├───index.html
│           └───results.html
│
└───templates/
    └───admin/
        └───base_site.html
```

---

## Requisitos

- Python 3.10 o superior
- Django 5.x
- Navegador web actualizado
- Editor de código (como Visual Studio Code)

---

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio:

```bash
git clone https://github.com/SantinoRodriguez/Preentrega-Django.git
cd Preentrega-Django/djangotutorial
```

### 2. Crear y activar un entorno virtual:

```bash
python -m venv env
env\Scripts\activate  # En Windows
```

### 3. Instalar Django:

```bash
pip install django
```

### 4. Aplicar migraciones iniciales:

```bash
python manage.py migrate
```

### 5. Crear un superusuario:

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

### 7. Abrir en el navegador:

- `http://127.0.0.1:8000/polls/`
- `http://127.0.0.1:8000/admin/`

---

Proyecto realizado por estudiantes como entrega práctica de la **PIA** para la materia *Laboratorio de Algoritmos y Estructura de Datos*.

Basado en el [Tutorial oficial de Django](https://docs.djangoproject.com/en/stable/intro/tutorial01/).

---

## Repositorio

```bash
git clone https://github.com/SantinoRodriguez/Preentrega-Django.git
```
