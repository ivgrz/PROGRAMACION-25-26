"""
Escribir un programa que almacene as asignaturas dun
curso (por exemplo Matemáticas, Física, Química, Historia
e Língua) nunha lista, pregunte o usuario a nota que
sacou en cada asignatura e elimine da lista as asignaturas
aprobadas. O fin, o programa debe mostrar por pantalla
as asignaturas que o usuario ten que repetir.

"""

def asignaturasaprob():

    asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]

    susp = [] #Lista que sirve para guardar las asignaturas que tengan menos de 5

    for asignatura in asignaturas:
        nota = float(input(f"Escribe las notas que sacaste en {asignatura}: "))

        if nota < 5:
            susp.append(asignatura)
    if susp:

        print(f"\n Tienes que repetir estas materias: ")
        for materia in susp:
                print(materia)
    else:
        print(f"\n Aprobaste todo")







asignaturasaprob()