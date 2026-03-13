from contacto import Contacto
from Agenda import Agenda


if __name__ == "__main__":
    a = Agenda()

    while True:
        print("\n1. Añadir contacto")
        print("2. Mostrar contactos")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            try:
                email = input("Email: ")
                c = Contacto(email)
                tf = input("Telefono (+nnnnnnnnnnn): ")
                c.anadir_telefono(tf)
                a.anadir_contactos(c)
                print("Contacto añadido.")
            except (TypeError, ValueError) as e:
                print(f"Error: {e}")

        elif opcion == "2":
            a.mostrar_contactos()

        elif opcion == "3":
            a.guardar_json_contactos()
            print("Agenda guardada. Hasta luego.")
            break
