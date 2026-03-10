# Crear unha aplicación para anotar tarefas para facer. A tarefa terá unha data,
# hora, duración, Nome da tarefa, descrición, estado(feita, non feita). Para iso
# crear unha clase Tarefa que manexe os datos relacionados coa tarefa. O
# usuario poderá facer as seguintes operacións:
# ●
# Agregar unha nova tarefa.
# ●
# Borrar unha tarefa.
# ●
# Modificar unha tarefa.
# ●
# Listar o listado de tarefas.
# ●
# As tarefas se gardarán nun ficheiro binario chamado tarefas.dat.

import datetime
import pickle


class Tarea:
    def __init__(self, fecha, hora, nombre, descripcion, estado: bool):
        self.fecha = fecha
        self.hora = hora
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.tareas = []

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        if not isinstance(fecha, datetime.date):
            raise TypeError("Formato invalido")
        self.__fecha = fecha

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        if not isinstance(hora, datetime.time):
            raise TypeError("Formato invalido")
        self.__hora = hora

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("Formato invalido")
        self.__nombre = nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        if not isinstance(descripcion, str):
            raise TypeError("Formato invalido")
        self.__descripcion = descripcion

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        if not isinstance(estado, bool):
            raise TypeError("Formato invalido")
        self.__estado = estado

    def agregar_tarea(self, tarea):
        if not isinstance(tarea, Tarea):
            raise TypeError(
                "Solo puedes añadir tareas con el formato adecuado")
        self.tareas.append(tarea)
# Remove borra un elemento en especifico dentro de una lista sin tener que hacer un for

    def borrar_tareas(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)

    def modificar_tarea(self, tarea):
        if tarea in self.tareas:
            while True:
                print("Que quieres modificar?\n"
                      "1. Fecha"
                      "2. Hora"
                      "3. Nombre"
                      "4. Descripcion"
                      "5. Estado"
                      "6. salir")
                opcion = input(": ")
                match opcion:
                    case '1':
                        nueva_fecha = input("Coloca la nueva fecha: ")
                        self.fecha = nueva_fecha
                    case '2':
                        nueva_hora = input("Coloca una nueva hora: ")
                        self.hora = nueva_hora
                    case '3':
                        nuevo_nombre = input(
                            "Coloca un nuevo nombre para la tarea: ")
                        self.nombre = nuevo_nombre
                    case '4':
                        n_descripcion = input("Cambia la descripcion aqui: ")
                        self.descripcion = n_descripcion
                    case '5':
                        n_estado = input(
                            "Cambia el estado actual (hecha-no_hecha): ")
                        self.estado = n_estado
                    case '6':
                        print("Saliendo...")
                        break
                    case _:
                        print("Opcion no valida")

    def guardar_tarea_fichero_binario(self):
        with open("tareas.dat", 'wb') as f:
            pickle.dump(self.tareas, f)

    def leer_fichero_binario(self):
        with open("tareas.dat", "rb") as f:
            self.tareas = pickle.load(f)

    def __str__(self):
        estado_str = "Hecha" if self.estado == True else "No-hecha"
        return (f"Fecha: {self.fecha}\nHora: {self.hora}\nNombre: {self.nombre}\nDescripcion: {self.descripcion}\n Estado: {estado_str}")
