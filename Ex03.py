soma = 0
numero = int(input("Digite um número inteiro: "))

while numero >= 0:
    soma += numero
    numero = int(input("Digite outro número inteiro (negativo para encerrar): "))

print(f"A soma dos números digitados é {soma}")