from servicios.inventario import Inventario
from modelo.producto import Producto

def menu():
    inv = Inventario()
    
    while True:
        print("\n--- SISTEMA DE INVENTARIO MI TIENDA LPQ ---")
        print("1. Añadir Producto Nuevo")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Lista Inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID: ")
                nom = input("Nombre: ")
                stock = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                inv.añadir_producto(Producto(id_p, nom, cant, prec))
            except ValueError:
                print("[Error] Entrada inválida. Cantidad y Precio deben ser números.")

        elif opcion == "2":
            id_p = input("ID del producto a actualizar: ")
            try:
                c = input("Nueva cantidad (vacío para omitir): ")
                p = input("Nuevo precio (vacío para omitir): ")
                cant = int(c) if c else None
                prec = float(p) if p else None
                inv.actualizar_producto(id_p, cant, prec)
            except ValueError:
                print("[Error] Ingrese valores numéricos válidos.")

        elif opcion == "3":
            id_p = input("ID del producto a eliminar: ")
            inv.eliminar_producto(id_p)

        elif opcion == "4":
            if not inv.productos:
                print("El inventario está vacío.")
            else:
                for p in inv.productos.values():
                    print(f"ID: {p.id_prod} | {p.nombre} | Cant: {p.cantidad} | ${p.precio}")

        elif opcion == "5":
            print("Salio del sistema mi TIENDA LPQ . ¡Vuelva pronto!")
            break
        else:
            print("Opción inválida, intente de nuevo.")
if __name__ == "__main__":
    menu()