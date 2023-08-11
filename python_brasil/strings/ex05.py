"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""


def nome_escada_invertida(nome):
    for i in range(len(nome), 0, -1):
        print(nome[:i])


nome_usuario = input('Digite seu nome: ')
nome_escada_invertida(nome_usuario)
