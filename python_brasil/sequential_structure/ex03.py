"""
Faça um Programa que peça dois números e imprima a soma.
"""

def soma(n1, n2):
    if n1.is_integer() and n2.is_integer():
        return int(n1 + n2)
    else:
        return n1 + n2

def is_numeric(entrada):
    try:
        float(entrada)
        return True
    except ValueError:
        return False

while True:
    number_1 = input('Digite o primeiro número: ')
    if is_numeric(number_1):
        break
    else:
        print("Entrada inválida. Tente novamente.")

while True:
    number_2 = input('Digite o segundo número: ')
    if is_numeric(number_2):
        break
    else:
        print("Entrada inválida. Tente novamente.")

number_1 = float(number_1)
number_2 = float(number_2)

resultado = soma(number_1, number_2)
print("A soma é:", resultado)

