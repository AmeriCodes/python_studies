"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

def titulo(msg):
    tam = len(msg) + 10
    print('~' * tam)
    print(f'     {msg}')
    print('~' * tam)
    return ''

pi = 3.14

print(titulo('ÁREA DO CÍRCULO'))

while True:
    try:
        raio = float(input('Digite o raio do círculo[m]: '))
        break
    except ValueError:
        print('Entrada inválida.')
        continue

area = pi * raio ** 2

print(f'De acordo com o raio fornecido\nA área desse círculo seria aproximadamente {area:.2f}m²')

