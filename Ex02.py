import random

numero_secreto = random.randint(1, 100)
numero = int(input("Digite um número entre 1 e 100: "))

while numero != numero_secreto:
    print("Número incorreto. Tente novamente.")
    numero = int(input("Digite um número entre 1 e 100: "))

print("Parabéns, você acertou!")