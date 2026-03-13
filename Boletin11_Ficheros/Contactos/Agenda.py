"""
Crea unha axenda de contactos onde cada contacto teña varios teléfonos e
un correo. A axenda ten que estar gardada nun ficheiro en formato json.
●
O programa debe permitir engadir novos contactos a unha lista de
dicionarios.
●
Ao saír, debe gardar toda a lista en axenda.json.
●
Ao volver abrir o programa, debe cargar os datos existentes para non
perdelos


"""
from contacto import Contacto
import os
import json


class Agenda:
    def __init__(self):
        self.contactos = []
        if os.path.exists("agenda.json"):
            with open("agenda.json", "r") as f:
                self.contactos = json.load(f)

    def anadir_contactos(self, contacto):
        if not isinstance(contacto, Contacto):
            raise ValueError("Añadir solo contactos validos")
        self.contactos.append(
            {"email": contacto.email, "telefonos": contacto.telefonos})

    def guardar_json_contactos(self):
        with open("agenda.json", "w", encoding='utf-8') as f:
            json.dump(self.contactos, f, indent=4)

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        for c in self.contactos:
            print(f"Email: {c['email']} | Teléfonos: {', '.join(c['telefonos'])}")
