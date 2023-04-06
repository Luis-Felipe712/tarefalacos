p = float(input("Digite o valor inicial a ser guardado: "))
i = 0.005  
n = 12 

for mes in range(1, n+1):
    m = p * (1 + i)**mes
    print(f"No mês {mes}, o montante é R${m:.2f}")