"""
A função 'print' exibe algo na tela, ela pode acumular vários argumentos, é só separa-los por vírgula, por padão, o python vai dar um espaço entre os argumentos, mas isso pode ser mudado utilizando o comando 'sep="?"', o que for colocado dentro das aspas será utilizado como separador; e o comando end='' serve para quebrar linhas.
"""

# \r\n = CRLF
print(12, 34, 1011, sep="-", end='##\r\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep= '&&')