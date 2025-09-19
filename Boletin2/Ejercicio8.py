"""
Fai o algoritmo e programa que calcule o soldo bruto e líquido, a percibir por unha
persoa. Para iso hai que ter en conta, que o soldo total inclúe os seguintes
conceptos:
● Soldo fixo.
● Comisión: 5% sobre importe total de vendas
● Quilometraxe: 2 € por km
● Dietas: 30 € por día de desprazamento.
Para calcular o soldo líquido debemos descontarlle ao soldo bruto:
● I.R.P.F. = 18 % do soldo total.
● Retención a seguridade social : 36 €.
"""

def calculo_sueldo():

  sueldo_fijo = float(input(f"Introduce tu sueldo fijo:"))
  importe_ventas = float(input(f"Introduce el importe total de ventas:"))
  kilometro = float(input(f"Introduce los kilometros recorridos:"))
  diaz_d = int(input(f"Introduce los dias de desplazamiento:"))
    # Calculamos el sueldo bruto
  comision = (importe_ventas * 0.05)
  kilometraje = (kilometro * 2)
  dietas = (diaz_d * 30)
  sueldo_bruto = (sueldo_fijo + comision + kilometraje + dietas)

  IRPF = (sueldo_bruto * 0.18)
  r_ss = 36
  sueldo_neto = (sueldo_bruto - IRPF - r_ss)

  print(f"Tu sueldo bruto es de {sueldo_bruto} y el neto es de {sueldo_neto}")

calculo_sueldo()
