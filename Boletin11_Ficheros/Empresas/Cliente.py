"""
Os obxectos Cliente se recollerán nunha lista.
A aplicación terá un menú que posibilitará as seguintes opcións:
●
●
●
●
Engadir novo cliente
Modificar datos
Dar de baixa clientes.
Listar os clientes.
A información se gardará nun ficheiro binario, que cargará en memoria o
iniciar o programa e se gardará en disco, actualizado o rematar.

"""
import pickle


class Cliente:

    clientes = []

    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        Cliente.clientes.append(self)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise TypeError("id con tipo invalido")
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("nombre con tipo invalido")
        self.__nombre = nombre

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        if not isinstance(telefono, int):
            raise TypeError("telefono con tipo invalido")
        self.__telefono = telefono

    def modificar_datos(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Solo se pueden modificar clientes ya creados")
        if cliente not in self.clientes:
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
        if cliente in self.clientes:
            Cliente.clientes.remove(cliente)
            print("Cliente dado de baja correctamente :D ")

    def guardar_fichero_binario(self):
        with open("cliente.dat", "wb") as f:
            pickle.dump(self.clientes, f)

    def leer_ficheros_binarios(self):
        with open("cliente.dat", "rb") as f:
            Cliente.clientes = pickle.load(f)

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Teléfono: {self.telefono}"


if __name__ == "__main__":
    c = Cliente(1, "Juan", 674674674)
