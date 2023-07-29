"""
Faça um Programa que peça um número e então mostre a mensagem 'O número informado foi [número]'.
"""

question = ''

while True:
    try:
        question = int(input('Digite um número: '))
        break
    except ValueError:
        print('Digite um número inteiro válido.')

print(f'O número digitado foi {question}')
