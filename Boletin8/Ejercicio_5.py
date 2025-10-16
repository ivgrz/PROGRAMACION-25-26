"""
Modificar as funcións anteriores para que teñan en conta o xénero do
destinatario, para elo, deberán recibir unha tupla de tuplas, contendo o nome
e o xénero, adaptando a mensaxe con ‘don’ ou ‘dona’ dependendo deste.
"""
def saludon(personas):

    for persona in personas:
        nombre = persona[0]
        genero = persona[1].upper()



        if genero == "M":
            saludo = "Estimado don"
        elif genero == "F":
            saludo = "Estimada doña"
        else:
            saludo = "Estimado/da/otro"

        print(f"{saludo} {nombre}")

datos_personas = (("Ana","F"), ("Juan", "M"), ("Maria","F"),("Alicia","F"),("Sol","F"))

saludon(datos_personas)
