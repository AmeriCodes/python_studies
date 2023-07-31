"""
Faça um Programa que converta metros para centímetros.
"""

def titulo(msg):
    tam = len(msg) + 10
    print('~' * tam)
    print(f'     {msg}')
    return print('~' * tam)


titulo('CONVERSÃO PARA CM')


while True:
    entrada = input("Digite o valor em metros: ")
    try:
        entrada = float(entrada)
        break
    except ValueError:
        print('Digite em metros.')
        continue


conversao = entrada * 100

print(f'Resulta em {conversao:.0f}Cm')

