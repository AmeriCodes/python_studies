"""
Data por extenso. Faça um programa que solicite a data de nascimento 
(dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

import os
from time import sleep

months = {
    '01': 'Janeiro',
    '02': 'Fevereiro',
    '03': 'Março',
    '04': 'Abril',
    '05': 'Maio',
    '06': 'Junho',
    '07': 'Julho',
    '08': 'Agosto',
    '09': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}

while True:
    entry = input('Data de nascimento (dd/mm/aaaa): ')

    if len(entry) == 10 and entry[2] == '/' and entry[5] == '/':
        day = entry[0:2]
        month = entry[3:5]
        year = entry[6:10]

        if month in months:
            month_name = months[month]
            print(f'Você nasceu em {day} de {month_name} de {year}')
            break
        else:
            print('Mês inválido. Tente novamente.')
            sleep(2)
            os.system('clear')
    else:
        print('Formato inválido. Tente novamente.')
        sleep(2)
        os.system('clear')