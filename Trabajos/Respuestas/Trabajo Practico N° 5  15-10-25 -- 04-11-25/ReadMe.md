# Nadie se salva solo - Sistema de Gestión de Tienda de Cómics

## Descripción del Proyecto

Sistema de gestión para la tienda de cómics "Nadie se salva solo" ubicada en San Telmo. Este proyecto implementa el núcleo lógico de una tienda online utilizando estructuras de datos eficientes para la gestión de inventario, procesamiento de pedidos y navegación de productos.

El sistema funciona completamente por consola y está diseñado para ser eficiente en operaciones críticas como búsqueda de productos, procesamiento de pedidos y mantenimiento del historial de navegación.

## Características Principales

- ✅ Gestión completa de inventario (agregar, actualizar, eliminar productos)
- ✅ Sistema de códigos únicos automático para cada producto
- ✅ Procesamiento de pedidos en orden FIFO
- ✅ Historial de últimos 5 productos visitados
- ✅ Categorización jerárquica (Marca → Categoría → Subcategoría)
- ✅ Búsqueda eficiente por código y categoría
- ✅ Persistencia de datos en formato JSON

## Requisitos

- Python 3.7 o superior
- No requiere librerías externas (solo módulos estándar de Python)

## Instrucciones de Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/usuario/nadie-se-salva-solo.git
cd nadie-se-salva-solo
```

### 2. Ejecutar el programa
```bash
python main.py
```

### 3. Navegación del menú

El sistema presenta un menú interactivo con las siguientes opciones:
```
1. Agregar producto al inventario
2. Agregar stock a producto existente
3. Eliminar producto
4. Recibir pedido
5. Procesar pedidos
6. Mostrar pedidos en cola
7. Mostrar historial de productos vistos
8. Buscar productos por categoría
9. Ver todas las categorías
10. Guardar y salir
```

### 4. Ejemplo de uso

**Agregar un producto:**
```
Opción: 1
Nombre del producto: Batman Dark Knight
Precio: 2500
Cantidad: 10
Marca: DC Comics
Categoría: Superhéroes
Subcategoría: Batman
```

**Recibir y procesar pedidos:**
```
Opción: 4
Producto solicitado: Batman Dark Knight

Opción: 5
[Se procesa el pedido y se actualiza el stock]
```

## Decisiones de Diseño

### 1. Hash Table - Gestión de Productos

**Estructura utilizada:** Hash Table

**Justificación:**
- Permite búsquedas, inserciones y eliminaciones en tiempo promedio **O(1)**
- La función hash utiliza la suma de valores ASCII de los caracteres del nombre del producto, aplicando módulo 10
- Se utiliza una lista de 10 buckets donde cada bucket contiene una lista de productos (manejo de colisiones por encadenamiento)
- Ideal para la búsqueda rápida por código único de producto

**Implementación:**
```python
def hash(Producto):
    return sum(ord(char) for char in str(Producto)) % 10
```

**Complejidad temporal:**
- Búsqueda: O(1) promedio, O(n) peor caso
- Inserción: O(1) promedio
- Eliminación: O(1) promedio

### 2. Queue (Cola) - Procesamiento de Pedidos

**Estructura utilizada:** Lista de Python como Queue (FIFO)

**Justificación:**
- Los pedidos deben procesarse en el orden exacto en que llegan (First In, First Out)
- Se utiliza `append()` para agregar pedidos al final y `pop(0)` para procesar el primero
- Garantiza justicia en el procesamiento: el primer cliente en solicitar es el primero en ser atendido

**Implementación:**
```python
pedidos = []  # Cola de pedidos

def RecibirPedido(Pedido):
    pedidos.append(Pedido.title())

def ProcesarPedidos():
    while pedidos:
        PedidoAtendido = pedidos.pop(0)  # FIFO
        # Procesar pedido...
```

**Complejidad temporal:**
- Encolar (append): O(1)
- Desencolar (pop(0)): O(n) - *Nota: podría optimizarse con collections.deque*

### 3. Stack (Pila) - Historial de Productos Vistos

**Estructura utilizada:** Lista de Python como Stack (LIFO) con tamaño máximo

**Justificación:**
- Mantiene los últimos 5 productos visitados por el cliente
- Los productos más recientes se agregan al final (`append()`)
- Cuando se excede el límite de 5, se elimina el más antiguo (`pop(0)`)
- Al mostrar el historial, se invierte el orden para mostrar del más reciente al más antiguo

**Implementación:**
```python
historialLista = []

def historial(Producto):
    historialLista.append(Producto)
    if len(historialLista) > 5:
        historialLista.pop(0)  # Eliminar el más antiguo

def mostrarHistorial():
    for Producto in reversed(historialLista):
        print(Producto)
```

**Complejidad temporal:**
- Agregar producto: O(1)
- Limitar tamaño: O(1)
- Mostrar historial: O(5) = O(1) constante

### 4. Tree (Árbol) - Categorización Jerárquica

**Estructura utilizada:** Árbol N-ario implementado con diccionarios anidados

**Justificación:**
- Representa la jerarquía: Marca → Categoría → Subcategoría → Productos
- Permite navegación eficiente por niveles jerárquicos
- Facilita búsquedas por cualquier nivel de la jerarquía
- Estructura dinámica que se construye automáticamente al agregar productos

**Implementación:**
```python
categorias = {
    "Comic": {
        "DC Comics": {
            "Batman": [producto1, producto2],
            "Superman": [producto3]
        }
    }
}
```

**Complejidad temporal:**
- Inserción: O(1) con acceso directo por claves
- Búsqueda por categoría: O(m) donde m es el número de productos en esa rama
- Reconstrucción del árbol: O(n) donde n es el total de productos

### 5. Persistencia de Datos - JSON

**Justificación:**
- Formato legible y fácil de editar manualmente si es necesario
- Compatibilidad nativa con Python (módulo `json`)
- Permite guardar y cargar la estructura completa de la tabla hash
- El árbol de categorías se reconstruye automáticamente al cargar los datos

## Estructura del Código
```
nadie-se-salva-solo/
│
├── main.py                 # Script principal con todas las clases
└── Stock.json             # Archivo de persistencia (se crea automáticamente)
README.md              # Este archivo
```

### Clases Principales

1. **Hash**: Gestiona la tabla hash de productos
   - `hash()`: Función hash para calcular posición
   - `agregar()`: Agrega nuevo producto con código único
   - `agregarProducto()`: Actualiza stock de producto existente
   - `eliminar()`: Elimina producto del inventario

2. **CategoriaArbol**: Gestiona la jerarquía de categorías
   - `agregar_arbol()`: Agrega producto al árbol de categorías
   - `eliminar_arbol()`: Elimina producto del árbol
   - `reconstruir_arbol()`: Reconstruye el árbol desde la tabla hash
   - `buscar_categoria()`: Busca productos por marca/categoría/subcategoría
   - `mostrar_todasCat()`: Muestra todas las categorías disponibles

3. **Pedidos**: Gestiona la cola de pedidos
   - `RecibirPedido()`: Agrega pedido a la cola
   - `ProcesarPedidos()`: Procesa todos los pedidos en orden FIFO
   - `MostrarPedidos()`: Muestra pedidos pendientes

4. **Historial**: Gestiona el historial de productos visitados
   - `historial()`: Agrega producto al historial (máx. 5)
   - `mostrarHistorial()`: Muestra historial en orden inverso

5. **Tienda**: Clase principal que integra todas las funcionalidades
   - `EjecutarMenu()`: Loop principal del sistema
   - Métodos privados para cada opción del menú

## Manejo de Errores

El sistema implementa manejo robusto de excepciones en todas las operaciones:
- Validación de entrada de datos (precios, cantidades)
- Manejo de archivos corruptos o inexistentes
- Protección contra interrupciones (Ctrl+C)
- Mensajes de error descriptivos para el usuario

## Ejemplos de Datos de Prueba
```python
# Productos de ejemplo
Batman Dark Knight - DC Comics - Superhéroes - Batman - $2500 - Stock: 10
Superman Origins - DC Comics - Superhéroes - Superman - $2200 - Stock: 5
Spider-Man Vol 1 - Marvel - Superhéroes - Spider-Man - $2800 - Stock: 8
```

## Bibliografía Consultada

1. **W3Schools - Data Structures and Algorithms**  
   https://www.w3schools.com/dsa/  
   Referencia principal para conceptos de estructuras de datos

2. **Python Documentation - Built-in Types**  
   https://docs.python.org/3/library/stdtypes.html  
   Documentación oficial de listas, diccionarios y estructuras nativas

3. **Python Documentation - JSON Module**  
   https://docs.python.org/3/library/json.html  
   Manejo de archivos JSON para persistencia

---

## Autores

Santino Luciano Rodriguez Fuchs
y
Luca Vigna.