class Contacto:

    def __init__(self, email):
        self.telefonos = []
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):

        if "@" not in email:
            raise TypeError("Formato de email invalido")
        else:
            self.__email = email

    def anadir_telefono(self, tf):

        numero = tf[3:]

        if not tf.startswith("+"):
            raise TypeError("Formato de numero invalido (+nnnnnnnnnnn)")
        elif len(numero) != 9:
            raise ValueError("Solo numeros de 9 digitos")
        elif not numero.isdigit():
            raise ValueError("El numero solo debe contener digitos")
        self.telefonos.append(tf)
