"""
O DNI ten unha parte numérica de i díxitos seguido dunha letra que
se obtén a partir do número da seguinte forma:
letra = número DNI % 22.
Baseándote nesta información, elixe a letra a partir da numeración da
seguinte táboa:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
T R W A G M Y F P D X B N J Z S Q V H L C K E
Deseña unha aplicación na que, dado un número de DNI, calcule a letra
que lle corresponde. Observa que un número de 8 díxitos entra dentro
do rango dun tipo int
"""

def dni():
    letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    dni_str = input("Dame tu numero de DNI:")
# Este es el rango valido para un DNI por los 8 digitos
    if len(dni_str) == 8 and dni_str.isdigit():
    # Calculamos la letra correspondiente al numero de DNI
        dni_num = int(dni_str)
    # el numero de DNI con el resto de la division entre 23 nos da la posicion de la letra en la lista
        letra = letras[dni_num % 23]
        print(f"Tu DNI es {dni_num}-{letra}")
    else:
        print("Debes introducir 8 digitos")
dni()
#Fin del codigo