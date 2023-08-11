"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

string_1 = str(input('Digite a primeira string: '))
string_2 = str(input('Digite a segunda string: '))

print(f'String 1: {string_1}"\nString 2: "{string_2}"')
print(f'Tamanho de "{string_1}": {len(string_1)} caracteres.',
      f'\nTamanho de "{string_2}": {len(string_2)} caracteres.')

if len(string_1) == len(string_2):
    print('As strings tem o mesmo comprimento.')
else:
    print('São de diferentes comprimentos.')

if string_1 == string_2:
    print('Tem o mesmo conteúdo. São idênticas.')
else:
    print('Não possuem o mesmo conteúdo. Há alguma diferênça.')