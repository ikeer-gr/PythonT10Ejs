import os

def crear_listin():
    """Crea el archivo listin.txt si no existe."""
    if not os.path.exists("./T10Ejercicios/listin.txt"):
        with open("listin.txt", "w") as f:
            pass

def consultar_cliente(nombre):
    """Consulta el teléfono de un cliente por su nombre."""
    try:
        with open("listin.txt", "r") as f:
            for linea in f:
                cliente, telefono = linea.strip().split(",")
                if cliente == nombre:
                    return telefono
        return "Cliente no encontrado."
    except FileNotFoundError:
        return "El listín no existe."

def agregar_cliente(nombre, telefono):
    """Añade un nuevo cliente y su teléfono al listín."""
    try:
        with open("listin.txt", "a") as f:
            f.write(f"{nombre},{telefono}\n")
        print("Cliente añadido correctamente.")
    except Exception as e:
        print(f"Error al agregar cliente: {e}")

def eliminar_cliente(nombre):
    """Elimina el teléfono de un cliente por su nombre."""
    try:
        clientes = []
        encontrado = False
        with open("listin.txt", "r") as f:
            for linea in f:
                cliente, telefono = linea.strip().split(",")
                if cliente != nombre:
                    clientes.append((cliente, telefono))
                else:
                    encontrado = True
        
        if encontrado:
            with open("listin.txt", "w") as f:
                for cliente, telefono in clientes:
                    f.write(f"{cliente},{telefono}\n")
            print("Cliente eliminado correctamente.")
        else:
            print("Cliente no encontrado.")
    except FileNotFoundError:
        print("El listín no existe.")
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")

def menu():
    """Muestra el menú del programa y gestiona las opciones."""
    while True:
        print("\n--- Listín Telefónico ---")
        print("1. Crear listín")
        print("2. Consultar cliente")
        print("3. Agregar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_listin()
            print("Listín creado/existente.")
        elif opcion == "2":
            nombre = input("Introduce el nombre del cliente: ")
            print(f"Teléfono: {consultar_cliente(nombre)}")
        elif opcion == "3":
            nombre = input("Introduce el nombre del cliente: ")
            telefono = input("Introduce el teléfono del cliente: ")
            agregar_cliente(nombre, telefono)
        elif opcion == "4":
            nombre = input("Introduce el nombre del cliente a eliminar: ")
            eliminar_cliente(nombre)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
