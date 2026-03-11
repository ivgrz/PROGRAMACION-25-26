import pickle
from Cliente import Cliente


class Administrador:
    def __init__(self) -> None:
        pass

    def modificar_datos(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Solo se pueden modificar clientes ya creados")
        if cliente not in Cliente.clientes:
            print("El cliente no existe en esta lista")
            return
        while True:
            print(
                f"Que dato quieres modificar del cliente {cliente.nombre}")
            print(f"1. id")
            print("2. Nombre")
            print("3. Telefono")
            print("4. Salir")
            opcion = input("Elige: ")

            match opcion:
                case '1':
                    id_n = int(input("Cual es el nuevo id?: "))

                    cliente.id = id_n
                case '2':
                    nombre_n = input("Cual es el nuevo nombre?: ")

                    cliente.nombre = nombre_n
                case '3':
                    tf_n = int(input("Cual es el nuevo telf.?: "))

                    cliente.telefono = tf_n
                case '4':
                    print("Saliendo...")
                    break

    def baja_clientes(self, cliente):
        if cliente in Cliente.clientes:
            Cliente.clientes.remove(cliente)
            print("Cliente dado de baja correctamente :D ")

    def guardar_fichero_binario(self):
        with open("cliente.dat", "wb") as f:
            pickle.dump(Cliente.clientes, f)

    def leer_ficheros_binarios(self):
        with open("cliente.dat", "rb") as f:
            Cliente.clientes = pickle.load(f)

    def mostrar_clientes(self):
        for cliente in Cliente.clientes:
            print(cliente)
