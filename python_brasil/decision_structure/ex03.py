"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

def verificando_sexo():
    while True:
        try:
            print('~' * 24)
            entrada = input('Qual é o seu sexo [M/F]: ').strip()[0]
            if entrada.upper() == 'F':
                return 'Feminino'
            elif entrada.upper() == 'M':
                return 'Masculino'
            else:
                print ('Sexo Inválido\n(M)asculino\n(F)eminino.')
        except IndexError:
            print('Não deixe em branco\nDigite algo.')


print(verificando_sexo())
