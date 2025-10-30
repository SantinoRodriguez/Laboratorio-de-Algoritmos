import os
import json
os.system('cls')

def cargar_tabla():
    try:
        with open("Stock.json", "r", encoding="utf-8") as Archivo:
            Datos = json.load(Archivo)
            if "Productos" in Datos and len(Datos["Productos"]) == 10:
                return Datos["Productos"]
    except FileNotFoundError:
        print("Archivo Stock.json no encontrado. Se creará una tabla vacía.")
    except json.JSONDecodeError:
        print("Stock.json corrupto o mal formado. Se inicializa tabla vacía.")
    except Exception as e:
        print("Error al cargar Stock.json:", e)
    
    return [[] for _ in range(10)]

def guardar_tabla(TablaHash):
    Datos = {"Productos": TablaHash}
    try:
        with open("Stock.json", "w", encoding="utf-8") as Archivo:
            json.dump(Datos, Archivo, indent=4, ensure_ascii=False)
        print("Datos guardados correctamente en Stock.json")
    except Exception as e:
        print("Error al guardar Stock.json:", e)

TablaHash = cargar_tabla()

# Estructura de árbol de categorías y lista de categorías
category_tree = {}
all_categories = []

class Hash():
    @staticmethod
    def hash(Producto):
        try:
            # Asegurarse de trabajar con string
            Nombre = str(Producto)
            return sum(ord(char) for char in Nombre) % 10
        except Exception as e:
            print("Error calculando hash del producto:", e)
            return 0

    @staticmethod
    def agregar(Producto, Precio, Cantidad, Marca, Categoria, Subcategoria):
        try:
            Todos = [p for sub in TablaHash for p in sub]
            Posicion = Hash.hash(Producto)

            if Todos:
                Codigos = [int(Item["Codigo"][1:]) for Item in Todos if "Codigo" in Item and isinstance(Item["Codigo"], str) and Item["Codigo"].startswith("C")]
                NuevoCodigo = "C" + str(max(Codigos) + 1).zfill(3) if Codigos else "C001"
            else:
                NuevoCodigo = "C001"

            NuevoProducto = {
                "Codigo": NuevoCodigo,
                "Nombre": Producto.title(),
                "Precio": float(Precio),
                "Cantidad": int(Cantidad),
                "Marca": Marca.title(),
                "Categoria": Categoria.title(),
                "Subcategoria": Subcategoria.title(),
                "Hash": Posicion
            }

            TablaHash[Posicion].append(NuevoProducto)
            print("Producto agregado correctamente:", Producto.title(), "(", NuevoCodigo, ")")
            
            # Agregar al árbol de categorías
            CategoryTree.add_to_tree(NuevoProducto)
            
        except ValueError:
            print("Error: Precio o Cantidad con formato incorrecto.")
        except Exception as e:
            print("Error al agregar producto:", e)

    @staticmethod
    def agregarProducto(Producto, Cantidad):
        try:
            Posicion = Hash.hash(Producto)
            Lista = TablaHash[Posicion]

            for Item in Lista:
                if Item.get("Nombre", "").lower() == Producto.lower():
                    try:
                        Item["Cantidad"] = int(Item.get("Cantidad", 0)) + int(Cantidad)
                        print("Stock actual:", Item["Cantidad"])
                    except ValueError:
                        print("Cantidad a agregar inválida.")
                    return
            print("Producto no encontrado.")
        except Exception as e:
            print("Error al agregar stock al producto:", e)

    @staticmethod
    def eliminar(Producto):
        try:
            Posicion = Hash.hash(Producto)
            Lista = TablaHash[Posicion]

            for Item in Lista:
                if Item.get("Nombre", "").lower() == Producto.lower():
                    Lista.remove(Item)
                    print("Producto eliminado:", Producto.title())
                    
                    # Eliminar del árbol de categorías
                    CategoryTree.remove_from_tree(Item)
                    return
            
            print("Producto no encontrado.")
        except Exception as e:
            print("Error al eliminar producto:", e)

class CategoryTree:
    @staticmethod
    def add_to_tree(product):
        """Agregar producto al árbol de categorías"""
        try:
            brand = product["Marca"]
            category = product["Categoria"]
            subcategory = product.get("Subcategoria", "General")
            
            # Crear estructura si no existe
            if brand not in category_tree:
                category_tree[brand] = {}
            
            if category not in category_tree[brand]:
                category_tree[brand][category] = {}
            
            if subcategory not in category_tree[brand][category]:
                category_tree[brand][category][subcategory] = []
            
            # Agregar producto a la subcategoría
            category_tree[brand][category][subcategory].append(product)
            
            # Actualizar lista de categorías
            if brand not in all_categories:
                all_categories.append(brand)
            
            category_full = f"{brand} - {category}"
            if category_full not in all_categories:
                all_categories.append(category_full)
            
            subcategory_full = f"{brand} - {category} - {subcategory}"
            if subcategory_full not in all_categories:
                all_categories.append(subcategory_full)
                
        except Exception as e:
            print(f"Error al agregar producto al árbol: {e}")
    
    @staticmethod
    def remove_from_tree(product):
        """Eliminar producto del árbol de categorías"""
        try:
            brand = product["Marca"]
            category = product["Categoria"]
            subcategory = product.get("Subcategoria", "General")
            
            if brand in category_tree and category in category_tree[brand] and subcategory in category_tree[brand][category]:
                # Buscar y eliminar el producto
                category_tree[brand][category][subcategory] = [
                    p for p in category_tree[brand][category][subcategory] 
                    if p["Codigo"] != product["Codigo"]
                ]
                
                # Limpiar si quedó vacío
                if not category_tree[brand][category][subcategory]:
                    del category_tree[brand][category][subcategory]
                    
                if not category_tree[brand][category]:
                    del category_tree[brand][category]
                    
                if not category_tree[brand]:
                    del category_tree[brand]
                    
        except Exception as e:
            print(f"Error al eliminar producto del árbol: {e}")
    
    @staticmethod
    def rebuild_tree():
        """Reconstruir árbol de categorías desde la tabla hash"""
        try:
            global category_tree, all_categories
            category_tree = {}
            all_categories = []
            
            for bucket in TablaHash:
                for product in bucket:
                    CategoryTree.add_to_tree(product)
                    
            print("Árbol de categorías reconstruido correctamente.")
        except Exception as e:
            print(f"Error al reconstruir árbol: {e}")
    
    @staticmethod
    def search_by_category(search_term):
        """Buscar productos por marca, categoría o subcategoría"""
        try:
            search_term = search_term.title()
            results = []
            
            print(f"\n===== RESULTADOS PARA: {search_term} =====")
            
            # Buscar por marca
            if search_term in category_tree:
                print(f"\nMarca: {search_term}")
                for category, subcategories in category_tree[search_term].items():
                    print(f"  Categoria: {category}")
                    for subcategory, products in subcategories.items():
                        print(f"    Subcategoria: {subcategory}")
                        for product in products:
                            print(f"      - {product['Codigo']}: {product['Nombre']} | "
                                  f"${product['Precio']} | Stock: {product['Cantidad']}")
                            results.append(product)
            
            # Buscar por categoría en todas las marcas
            found_category = False
            for brand, categories in category_tree.items():
                if search_term in categories:
                    found_category = True
                    print(f"\nMarca: {brand} -> Categoria: {search_term}")
                    for subcategory, products in categories[search_term].items():
                        print(f"  Subcategoria: {subcategory}")
                        for product in products:
                            print(f"    - {product['Codigo']}: {product['Nombre']} | "
                                  f"${product['Precio']} | Stock: {product['Cantidad']}")
                            if product not in results:
                                results.append(product)
            
            # Buscar por subcategoría en todas las marcas y categorías
            found_subcategory = False
            for brand, categories in category_tree.items():
                for category, subcategories in categories.items():
                    if search_term in subcategories:
                        found_subcategory = True
                        print(f"\nMarca: {brand} -> Categoria: {category} -> Subcategoria: {search_term}")
                        for product in subcategories[search_term]:
                            print(f"  - {product['Codigo']}: {product['Nombre']} | "
                                  f"${product['Precio']} | Stock: {product['Cantidad']}")
                            if product not in results:
                                results.append(product)
            
            if not results:
                print("No se encontraron productos para esta categoría.")
            else:
                print(f"\nTotal encontrados: {len(results)}")
                
        except Exception as e:
            print(f"Error al buscar por categoría: {e}")
    
    @staticmethod
    def show_all_categories():
        """Mostrar todas las categorías disponibles"""
        try:
            print("\n===== CATEGORIAS DISPONIBLES =====")
            if not all_categories:
                print("No hay categorías registradas.")
                return
            
            print("\nMarcas y Categorias:")
            for category in sorted(all_categories):
                print(f"  - {category}")
        except Exception as e:
            print(f"Error al mostrar categorías: {e}")

pedidos = []

class Pedidos():
    def RecibirPedido(Pedido):
        try:
            pedidos.append(Pedido.title())
            print("Pedido agregado:", Pedido.title())
        except Exception as e:
            print("Error al recibir pedido:", e)

    def ProcesarPedidos():
        try:
            if not pedidos:
                print("No hay pedidos para procesar.")
                return

            while pedidos:
                PedidoAtendido = pedidos.pop(0)
                try:
                    Posicion = Hash.hash(PedidoAtendido)
                    Lista = TablaHash[Posicion]

                    encontrado = False
                    for Item in Lista:
                        if Item.get("Nombre", "").lower() == PedidoAtendido.lower():
                            encontrado = True
                            try:
                                Item["Cantidad"] = int(Item.get("Cantidad", 0)) - 1
                                print("Se atendió el pedido:", PedidoAtendido.title())
                                print("Stock restante:", Item["Cantidad"])
                            except ValueError:
                                print("Error: la cantidad del producto no es un entero válido.")
                            
                            if Item.get("Cantidad", 0) <= 0:
                                try:
                                    Lista.remove(Item)
                                    print("El producto se quedó sin stock y fue retirado.")
                                    CategoryTree.remove_from_tree(Item)
                                except Exception as e:
                                    print("Error al remover el producto sin stock:", e)
                            
                            Historial.historial(PedidoAtendido)
                            break

                    if not encontrado:
                        print("El producto solicitado no existe:", PedidoAtendido.title())

                except Exception as e:
                    print(f"Error procesando el pedido '{PedidoAtendido}':", e)

            print("No quedan pedidos por procesar.")
        except Exception as e:
            print("Error en ProcesarPedidos:", e)

    def MostrarPedidos():
        try:
            print("Pedidos en cola:", pedidos)
        except Exception as e:
            print("Error mostrando pedidos:", e)

historialLista = []

class Historial:
    def historial(Producto):
        try:
            historialLista.append(Producto)
            if len(historialLista) > 5:
                historialLista.pop(0)
        except Exception as e:
            print("Error actualizando historial:", e)

    def mostrarHistorial():
        try:
            print("Últimos productos pedidos:")
            for Producto in reversed(historialLista):
                print(Producto)
        except Exception as e:
            print("Error mostrando historial:", e)

# ------------------ MENU ------------------

# Reconstruir árbol de categorías al iniciar
CategoryTree.rebuild_tree()

while True:
    try:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Agregar producto al inventario")
        print("2. Agregar stock a producto existente")
        print("3. Eliminar producto")
        print("4. Recibir pedido")
        print("5. Procesar pedidos")
        print("6. Mostrar pedidos en cola")
        print("7. Mostrar historial de productos vistos")
        print("8. Buscar productos por categoria")
        print("9. Ver todas las categorias")
        print("10. Guardar y salir")

        Opcion = input("Seleccione una opción: ").strip()

        if Opcion == "1":
            try:
                Producto = input("Nombre del producto: ").strip()
                Precio_input = input("Precio: ").strip()
                Cantidad_input = input("Cantidad: ").strip()
                Marca = input("Marca: ").strip()
                Categoria = input("Categoria: ").strip()
                Subcategoria = input("Subcategoria: ").strip()
                # Intentar convertir antes de llamar
                Precio = float(Precio_input)
                Cantidad = int(Cantidad_input)
                Hash.agregar(Producto, Precio, Cantidad, Marca, Categoria, Subcategoria)
            except ValueError:
                print("Precio o Cantidad con formato inválido. Intente de nuevo.")
            except Exception as e:
                print("Error en opción 1:", e)

        elif Opcion == "2":
            try:
                Producto = input("Producto: ").strip()
                Cantidad_input = input("Cantidad a agregar: ").strip()
                Cantidad = int(Cantidad_input)
                Hash.agregarProducto(Producto, Cantidad)
            except ValueError:
                print("Cantidad inválida.")
            except Exception as e:
                print("Error en opción 2:", e)

        elif Opcion == "3":
            try:
                Producto = input("Producto a eliminar: ").strip()
                Hash.eliminar(Producto)
            except Exception as e:
                print("Error en opción 3:", e)

        elif Opcion == "4":
            try:
                Pedido = input("Producto solicitado: ").strip()
                Pedidos.RecibirPedido(Pedido)
            except Exception as e:
                print("Error en opción 4:", e)

        elif Opcion == "5":
            try:
                Pedidos.ProcesarPedidos()
            except Exception as e:
                print("Error en opción 5:", e)

        elif Opcion == "6":
            try:
                Pedidos.MostrarPedidos()
            except Exception as e:
                print("Error en opción 6:", e)

        elif Opcion == "7":
            try:
                Historial.mostrarHistorial()
            except Exception as e:
                print("Error en opción 7:", e)

        elif Opcion == "8":
            try:
                search_term = input("Ingrese marca, categoria o subcategoria a buscar: ").strip()
                if search_term:
                    CategoryTree.search_by_category(search_term)
                else:
                    print("Debe ingresar un término de búsqueda.")
            except Exception as e:
                print("Error en opción 8:", e)

        elif Opcion == "9":
            try:
                CategoryTree.show_all_categories()
            except Exception as e:
                print("Error en opción 9:", e)

        elif Opcion == "10":
            try:
                guardar_tabla(TablaHash)
                print("Saliendo del sistema.")
                break
            except Exception as e:
                print("Error guardando datos al salir:", e)

        else:
            print("Opción no válida. Intente de nuevo.")
    except KeyboardInterrupt:
        # Capturar Ctrl+C para guardar antes de salir
        try:
            print("\nInterrupción por teclado detectada. Guardando datos...")
            guardar_tabla(TablaHash)
        except Exception:
            pass
        print("Saliendo.")
        break
    except Exception as e:
        print("Error en el menú principal:", e)