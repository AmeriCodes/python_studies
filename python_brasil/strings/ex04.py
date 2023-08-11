"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""


def nome_escada(nome):
    novo_nome = ''
    for i in nome:
        novo_nome += i
        print(novo_nome)


nome_usuario = str(input('Digite seu nome: '))
nome_escada(nome_usuario)