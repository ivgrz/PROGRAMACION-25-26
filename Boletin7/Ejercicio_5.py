"""
 Conta as vocais e as consoantes do String “Python Python Python”.
Ollo cos espazos!
"""
def contar_vocal_consonantes():

    vocales = ["a","e","i","o","u"]
    sumv = 0

    sumc = 0

    texto = "Python Python Python"

    texto_sin_espacios = texto.replace(" ", "")

    textof = texto_sin_espacios.lower()

    for i in textof:
            if i in vocales: 
                sumv += 1
            elif i.isalpha(): #Si es letra pero no vocal sume solo 1 vez
                sumc += 1
    print(f"Analizamos este texto: {texto}")
    print(f"La cantidad de vocales es {sumv} y de consonantes son {sumc}")








contar_vocal_consonantes()