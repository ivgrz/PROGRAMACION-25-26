"""
Escribir un programa que almacene as asignaturas dun
curso (por exemplo Matemáticas, Física, Química, Historia
e Língua) nunha lista, pregunte o usuario a nota que
sacou en cada asignatura, e despois as mostre por
pantalla co mensaxe En <asignatura> sacaches <nota>
onde <asignatura> é cada unha das asignaturas da lista e
<nota> cada unha das correspondentes notas
introducidas polo usuario.

"""
def asignaturas():
    asignaturasl = ["Matematica","Fisica","Quimica","Historia","Lengua"]

    notas = []

    for asignatura in asignaturasl:
        nota = float(input(f"que nota sacaste en  {asignatura}: "))
        notas.append(nota)

    print(f"\n resultados")
    for i in range(len(asignaturasl)):
        print(f"En {asignaturasl[i]} sacaste {notas[i]}")



asignaturas()