import os
from modelo.producto import Producto

class Inventario:
    def __init__(self, nombre_archivo="inventario.txt"):
        self.productos = {}
        self.nombre_archivo = nombre_archivo
        # Se carga el archivo inmediatamente al instanciar la clase
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee el archivo .txt y reconstruye el diccionario en memoria."""
        try:
            if not os.path.exists(self.nombre_archivo):
                # Si no existe, creamos un archivo vacío
                with open(self.nombre_archivo, 'w', encoding='utf-8') as f:
                    pass
                print(f"[Aviso] El archivo '{self.nombre_archivo}' no existía. Se ha creado uno nuevo.")
                return

            with open(self.nombre_archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        # Manejo de archivos corruptos: validamos que la línea tenga 4 partes
                        partes = linea.split(',')
                        if len(partes) == 4:
                            id_p, nom, cant, prec = partes
                            self.productos[id_p] = Producto(id_p, nom, int(cant), float(prec))
            print("[Éxito] Inventario cargado correctamente desde el archivo.")

        except PermissionError:
            print("[Error] No se tienen permisos para leer el archivo de inventario.")
        except ValueError:
            print("[Error] El archivo contiene datos corruptos o con formato inválido.")
        except Exception as e:
            print(f"[Error Inesperado] {e}")

    def guardar_en_archivo(self):
        """Sobrescribe el archivo con el estado actual del diccionario productos."""
        try:
            with open(self.nombre_archivo, 'w', encoding='utf-8') as f:
                for p in self.productos.values():
                    f.write(str(p) + '\n')
            return True
        except PermissionError:
            print("[Error] Permiso denegado: No se pudo escribir en el archivo.")
            return False
        except Exception as e:
            print(f"[Error Crítico] Fallo al sincronizar con el disco: {e}")
            return False

    def añadir_producto(self, producto):
        if producto.id_prod in self.productos:
            print(f"[!] El ID {producto.id_prod} ya existe.")
            return
        
        self.productos[producto.id_prod] = producto
        if self.guardar_en_archivo():
            print(f"✓ '{producto.nombre}' añadido exitosamente al archivo.")

    def actualizar_producto(self, id_prod, cantidad=None, precio=None):
        if id_prod in self.productos:
            if cantidad is not None: self.productos[id_prod].cantidad = cantidad
            if precio is not None: self.productos[id_prod].precio = precio
            
            if self.guardar_en_archivo():
                print(f"✓ Producto {id_prod} actualizado y guardado.")
        else:
            print("[!] Producto no encontrado.")

    def eliminar_producto(self, id_prod):
        if id_prod in self.productos:
            del self.productos[id_prod]
            if self.guardar_en_archivo():
                print(f"✓ Producto {id_prod} eliminado correctamente.")
        else:
            print("[!] El ID proporcionado no existe.")