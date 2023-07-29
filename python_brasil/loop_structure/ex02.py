"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""


while True:
    nome = input('Usuário: ').strip()
    senha = input('Senha: ').strip()
    if senha.upper() == nome.upper():
        print('Por quenstão de segurança\nA senha não pode ser igual ao Usuário.')
        continue
    else:
        if len(senha) < 8:
            print('Por favor, senhas acima de 8 caracteres!')
            continue
        break