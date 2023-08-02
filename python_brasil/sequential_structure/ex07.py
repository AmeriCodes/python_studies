"""
Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.
"""

while True:
    try:
        lado = int(input("Digita a medida de um lado do quadrado: "))
        if lado > 0:
            break
        else:
            print("(Entrada inválida!)\nDigite apenas números positivos.")
            continue
    except ValueError:
        print("(Entrada inválida!)\nDigite apenas números inteiros.")
        continue


area = lado**2

print("-" * 30)
print(f"A área do quadrado seria {area}².")
print(f"O dobro da área desse quadrado seria {area * 2}².")
