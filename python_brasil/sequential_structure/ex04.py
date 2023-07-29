"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

def calculo_de_media(lita_de_notas):
    return sum(lita_de_notas) / len(lita_de_notas)



notas_bimestrais = []

for i in range(4):
    while True:
        nota = input(f'Digite a nota do {i + 1}º bimestre: ')
        if nota.replace('.','', 1).isdigit():
            notas_bimestrais.append(float(nota))
            break
        else:
            print('Nota inválida. Tente novamente.')


media = calculo_de_media(notas_bimestrais)
print(f"A média das notas bimestrais é: {media:.1f}")
