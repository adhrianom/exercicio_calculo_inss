import math

salario_bruto = float(input())
inss = 0

match salario_bruto:
    case n if salario_bruto <= 720.00:
        inss = salario_bruto * 0.0765
    case n if salario_bruto > 720.00 and salario_bruto <= 1200.00:
        inss = salario_bruto * 0.09
    case n if salario_bruto > 1200.00 and salario_bruto <= 2400.00:
        inss = salario_bruto * 0.11
    case _ :
        inss = (2400 * 0.11)

print(inss)