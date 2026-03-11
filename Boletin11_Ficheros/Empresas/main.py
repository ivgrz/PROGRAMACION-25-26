from Cliente import Cliente
from Administrador import Administrador

if __name__ == "__main__":
    A = Administrador()
    A.leer_ficheros_binarios()

    while True:
        print("\n1. Añadir cliente")
        print("2. Modificar cliente")
        print("3. Dar de baja cliente")
        print("4. Listar clientes")
        print("5. Salir")
        opcion = input("Elige: ")

        match opcion:
            case '1':
                id = int(input("ID: "))
                nombre = input("Nombre: ")
                telefono = int(input("Teléfono: "))
                Cliente(id, nombre, telefono)
                print("Cliente añadido correctamente")
            case '2':
                id = int(input("ID del cliente a modificar: "))
                cliente = next((c for c in Cliente.clientes if c.id == id), None)
                if cliente:
                    A.modificar_datos(cliente)
                else:
                    print("Cliente no encontrado")
            case '3':
                id = int(input("ID del cliente a dar de baja: "))
                cliente = next((c for c in Cliente.clientes if c.id == id), None)
                if cliente:
                    A.baja_clientes(cliente)
                else:
                    print("Cliente no encontrado")
            case '4':
                A.mostrar_clientes()
            case '5':
                A.guardar_fichero_binario()
                print("Datos guardados. Hasta luego!")
                break
