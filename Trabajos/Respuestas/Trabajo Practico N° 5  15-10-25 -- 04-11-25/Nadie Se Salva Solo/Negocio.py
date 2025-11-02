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

categorias = {}
TodasCat = []

class Hash():
    @staticmethod
    def hash(Producto):
        try:
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
            CategoriaArbol.agregar_arbol(NuevoProducto)
            
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
                    
                    CategoriaArbol.eliminar_arbol(Item)
                    return
            
            print("Producto no encontrado.")
        except Exception as e:
            print("Error al eliminar producto:", e)

class CategoriaArbol:
    @staticmethod
    def agregar_arbol(product):
        try:
            Separacion = product["Marca"]
            Categoria = product["Categoria"]
            Subcategoria = product.get("Subcategoria", "General")
            
            # Crear estructura si no existe
            if Separacion not in categorias:
                categorias[Separacion] = {}
            
            if Categoria not in categorias[Separacion]:
                categorias[Separacion][Categoria] = {}
            
            if Subcategoria not in categorias[Separacion][Categoria]:
                categorias[Separacion][Categoria][Subcategoria] = []
            
            categorias[Separacion][Categoria][Subcategoria].append(product)
            
            if Separacion not in TodasCat:
                TodasCat.append(Separacion)
            
            CategoriaFull = f"{Separacion} - {Categoria}"
            if CategoriaFull not in TodasCat:
                TodasCat.append(CategoriaFull)
            
            SubCategoriaFull = f"{Separacion} - {Categoria} - {Subcategoria}"
            if SubCategoriaFull not in TodasCat:
                TodasCat.append(SubCategoriaFull)
                
        except Exception as e:
            print(f"Error al agregar producto al árbol: {e}")
    
    @staticmethod
    def eliminar_arbol(product):
        try:
            Separacion = product["Marca"]
            Categoria = product["Categoria"]
            Subcategoria = product.get("Subcategoria", "General")
            
            if Separacion in categorias and Categoria in categorias[Separacion] and Subcategoria in categorias[Separacion][Categoria]:
                categorias[Separacion][Categoria][Subcategoria] = [
                    p for p in categorias[Separacion][Categoria][Subcategoria] 
                    if p["Codigo"] != product["Codigo"]
                ]
                
                if not categorias[Separacion][Categoria][Subcategoria]:
                    del categorias[Separacion][Categoria][Subcategoria]
                    
                if not categorias[Separacion][Categoria]:
                    del categorias[Separacion][Categoria]
                    
                if not categorias[Separacion]:
                    del categorias[Separacion]
                    
        except Exception as e:
            print(f"Error al eliminar producto del árbol: {e}")
    
    @staticmethod
    def reconstruir_arbol():
        try:
            global categorias, TodasCat
            categorias = {}
            TodasCat = []
            
            for bucket in TablaHash:
                for product in bucket:
                    CategoriaArbol.agregar_arbol(product)
                    
            print("Árbol de categorías reconstruido correctamente.")
        except Exception as e:
            print(f"Error al reconstruir árbol: {e}")
    
    @staticmethod
    def buscar_categoria(buscar_termino):
        try:
            buscar_termino = buscar_termino.title()
            resultado = []
            
            print(f"\n===== RESULTADOS PARA: {buscar_termino} =====")
            
            # Buscar por marca
            if buscar_termino in categorias:
                print(f"\nMarca: {buscar_termino}")
                for Categoria, subcategories in categorias[buscar_termino].items():
                    print(f"  Categoria: {Categoria}")
                    for Subcategoria, products in subcategories.items():
                        print(f"    Subcategoria: {Subcategoria}")
                        for product in products:
                            print(f"      - {product['Codigo']}: {product['Nombre']} | " f"${product['Precio']} | Stock: {product['Cantidad']}")
                            resultado.append(product)
            
            EncontrarCategoria = False
            for Separacion, categories in categorias.items():
                if buscar_termino in categories:
                    EncontrarCategoria = True
                    print(f"\nMarca: {Separacion} -> Categoria: {buscar_termino}")
                    for Subcategoria, products in categories[buscar_termino].items():
                        print(f"  Subcategoria: {Subcategoria}")
                        for product in products:
                            print(f"    - {product['Codigo']}: {product['Nombre']} | " f"${product['Precio']} | Stock: {product['Cantidad']}")
                            if product not in resultado:
                                resultado.append(product)
            
            EncontrarSubategoria = False
            for Separacion, categories in categorias.items():
                for Categoria, subcategories in categories.items():
                    if buscar_termino in subcategories:
                        EncontrarSubategoria = True
                        print(f"\nMarca: {Separacion} -> Categoria: {Categoria} -> Subcategoria: {buscar_termino}")
                        for product in subcategories[buscar_termino]:
                            print(f"  - {product['Codigo']}: {product['Nombre']} | " f"${product['Precio']} | Stock: {product['Cantidad']}")
                            if product not in resultado:
                                resultado.append(product)
            
            if not resultado:
                print("No se encontraron productos para esta categoría.")
            else:
                print(f"\nTotal encontrados: {len(resultado)}")
                
        except Exception as e:
            print(f"Error al buscar por categoría: {e}")
    
    @staticmethod
    def mostrar_todasCat():
        try:
            print("\n===== CATEGORIAS DISPONIBLES =====")
            if not TodasCat:
                print("No hay categorías registradas.")
                return
            
            print("\nMarcas y Categorias:")
            for Categoria in sorted(TodasCat):
                print(f"  - {Categoria}")
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
                                    CategoriaArbol.eliminar_arbol(Item)
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

class Tienda:
    def __init__(self, TablaHashRef, HashModule, PedidosModule, HistorialModule, CategoriaArbolModule, GuardarFunc):
        # Referencias a las estructuras / módulos externos
        self.TablaHash = TablaHashRef
        self.Hash = HashModule
        self.Pedidos = PedidosModule
        self.Historial = HistorialModule
        self.CategoriaArbol = CategoriaArbolModule
        self.GuardarFunc = GuardarFunc

        # Reconstruir árbol de categorías al iniciar (igual que en tu script actual)
        try:
            self.CategoriaArbol.reconstruir_arbol()
        except Exception as e:
            print("Error al reconstruir el árbol de categorías:".title(), e)

    def EjecutarMenu(self):
        """Bucle principal del menú (sustituye el bloque while True original)."""
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
                    self._opcion_agregar_producto()
                elif Opcion == "2":
                    self._opcion_agregar_stock()
                elif Opcion == "3":
                    self._opcion_eliminar_producto()
                elif Opcion == "4":
                    self._opcion_recibir_pedido()
                elif Opcion == "5":
                    self._opcion_procesar_pedidos()
                elif Opcion == "6":
                    self._opcion_mostrar_pedidos()
                elif Opcion == "7":
                    self._opcion_mostrar_historial()
                elif Opcion == "8":
                    self._opcion_buscar_categoria()
                elif Opcion == "9":
                    self._opcion_mostrar_todas_categorias()
                elif Opcion == "10":
                    try:
                        self.GuardarFunc(self.TablaHash)
                        print("Saliendo del sistema.".title())
                        break
                    except Exception as e:
                        print("Error guardando datos al salir:".title(), e)
                else:
                    print("Opción no válida. Intente de nuevo.".title())

            except KeyboardInterrupt:
                # Capturar Ctrl+C para guardar antes de salir
                try:
                    print("\nInterrupción por teclado detectada. Guardando datos...".title())
                    self.GuardarFunc(self.TablaHash)
                except Exception:
                    pass
                print("Saliendo.".title())
                break
            except Exception as e:
                print("Error en el menú principal:".title(), e)

    # ---------------- Métodos para cada opción ----------------

    def _opcion_agregar_producto(self):
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

            # Llamada al método estático/agregado de tu Hash (igual que antes)
            self.Hash.agregar(Producto, Precio, Cantidad, Marca, Categoria, Subcategoria)

        except ValueError:
            print("Precio o Cantidad con formato inválido. Intente de nuevo.".title())
        except Exception as e:
            print("Error en opción 1:".title(), e)

    def _opcion_agregar_stock(self):
        try:
            Producto = input("Producto: ").strip()
            Cantidad_input = input("Cantidad a agregar: ").strip()
            Cantidad = int(Cantidad_input)
            self.Hash.agregarProducto(Producto, Cantidad)
        except ValueError:
            print("Cantidad inválida.".title())
        except Exception as e:
            print("Error en opción 2:".title(), e)

    def _opcion_eliminar_producto(self):
        try:
            Producto = input("Producto a eliminar: ").strip()
            self.Hash.eliminar(Producto)
        except Exception as e:
            print("Error en opción 3:".title(), e)

    def _opcion_recibir_pedido(self):
        try:
            Pedido = input("Producto solicitado: ").strip()
            self.Pedidos.RecibirPedido(Pedido)
        except Exception as e:
            print("Error en opción 4:".title(), e)

    def _opcion_procesar_pedidos(self):
        try:
            self.Pedidos.ProcesarPedidos()
        except Exception as e:
            print("Error en opción 5:".title(), e)

    def _opcion_mostrar_pedidos(self):
        try:
            self.Pedidos.MostrarPedidos()
        except Exception as e:
            print("Error en opción 6:".title(), e)

    def _opcion_mostrar_historial(self):
        try:
            self.Historial.mostrarHistorial()
        except Exception as e:
            print("Error en opción 7:".title(), e)

    def _opcion_buscar_categoria(self):
        try:
            buscar_termino = input("Ingrese marca, categoria o Subcategoria a buscar: ").strip()
            if buscar_termino:
                self.CategoriaArbol.buscar_categoria(buscar_termino)
            else:
                print("Debe ingresar un término de búsqueda.".title())
        except Exception as e:
            print("Error en opción 8:".title(), e)

    def _opcion_mostrar_todas_categorias(self):
        try:
            self.CategoriaArbol.mostrar_todasCat()
        except Exception as e:
            print("Error en opción 9:".title(), e)

if __name__ == "__main__":
    Sistema = Tienda(TablaHash, Hash, Pedidos, Historial, CategoriaArbol, guardar_tabla)
    Sistema.EjecutarMenu()