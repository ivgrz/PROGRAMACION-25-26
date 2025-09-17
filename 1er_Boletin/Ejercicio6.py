'''
Mostrar o resultado de executar estes bloques de código no intérprete de
python:
  for i in range(5):
...     print(i * i)
 for i in range(2,6):
...     print(i, 2**i)
 for d in [3, 1, 4, 1, 5]:
...     print(d,)
'''


def main():
    tabla = [3,1,4,1,5]

    print("Resultado del primer bloque de código:")
    for i in range(5):
        print(i * i)
    print("\n")
    print("Resultado del segundo bloque de código:")
    for i in range(2,6):
        print(i , 2**i)
    print("\n")
    print("Resultado del tercer bloque de código:")
    for d in tabla:
        print(d, end=" ")
    print("\n")

if __name__ == "__main__":
    main()



