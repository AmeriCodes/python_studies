"""
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""


def nome_invertido_maiusculo(nome):
    nome_invertido = nome[::-1]
    nome_maiusculo = nome_invertido.upper()
    return nome_maiusculo


nome = str(input('Digite seu nome: '))
resultado = nome_invertido_maiusculo(nome)
print(f'Nome invertido em maiúsculos é: {resultado}')