"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input('Nome: ').strip()
    if len(nome) < 3:
        print('3 caracteres no mínimo!\nDigite de novo.')
        continue
    else:
        break

while True:
    try:
        idade = int(input('Idade: '))
        if idade < 0 or idade > 150:
            print('Por favor.\nDigite sua idade verdadeira.')
            continue
        else:
            break
    except ValueError:
        print('Digite a idade em anos.')
        continue

while True:
    salario = float(input('Salário: '))
    if salario < 0:
        print('Digite um valor válido: ')
        continue
    else:
        break

while True:
    sexo = input('Sexo[M/F]: ').strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Digite gêneros existentes.\nNão é difícil, só há dois.')
        continue


while True:
    estado_civil = input(
        'Digite seu estado civil: \n'
        '[C]asado(a)\n'
        '[S]olteiro(a)\n'
        '[V]iuvo(a)\n'
        '[D]vivorciado(a)\n'
        ':'
        ).strip().upper()[0]
    if estado_civil not in 'CSVD':
        print('Digite as opções citadas.')
        continue
    else:
        break

