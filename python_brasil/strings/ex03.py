"""
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
"""

def nome_na_vertical(nome):
    for i in nome:
        print(i)


nome_usuario = str(input('Digite o nome: '))

nome_na_vertical(nome_usuario)