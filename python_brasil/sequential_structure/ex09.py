"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


def titulo(msg):
    tam = len(msg) + 10
    print('~' * tam)
    print(f'     {msg}')
    return print('~' * tam)


titulo('Fahrenheit >>> Celsius')
while True:
    try:
        entry = int(input('Digite os graus Fº: '))
        break
    except ValueError:
        print('Digite apenas números inteiros!')
        continue


celsius = 5 * ((entry - 32) / 9)


print(f'{entry}º Fahrenheit são {celsius:.1f}º Celsius.')