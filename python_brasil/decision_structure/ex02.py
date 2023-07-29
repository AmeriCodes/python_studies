"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

number = 0

while True:
    try:
        number = int(input('Digite um número: '))
        break
    except ValueError:
        print('Digite número!')

if number > 0:
    print(f'{number} é positivo.')
else:
    print(f'{number} é negativo.')

