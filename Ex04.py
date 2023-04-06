import random

num_jogadas = int(input("Digite o número de vezes que você quer jogar a moeda: "))
caras = 0
coroas = 0

for i in range(num_jogadas):
    resultado = random.randint(0, 1)
    if resultado == 0:
        print("Cara")
        caras += 1
    else:
        print("Coroa")
        coroas += 1

print(f"Total de caras: {caras}")
print(f"Total de coroas: {coroas}")