"""
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""


def salario_mes(salario, horas):
    return f"{salario * horas:.2f}"


while True:
    try:
        money = float(input("Salario por hora: "))
        break
    except ValueError:
        print("Entrada inválida.")
    continue

while True:
    try:
        worked_hours_this_month = float(input("Horas trabalhadas no mês: "))
        break
    except ValueError:
        print("Entrada inválida.")
    continue


print(salario_mes(money, worked_hours_this_month))
