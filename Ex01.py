valor = int(input("Digite um valor entre 1 e 10: "))

while valor < 1 or valor > 10:
    valor = int(input("Valor inválido. Digite um valor entre 1 e 10: "))

for i in range(1, 11):
    print(f"{valor} x {i} = {valor * i}")