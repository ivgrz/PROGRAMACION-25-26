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

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Teléfono: {self.telefono}"
