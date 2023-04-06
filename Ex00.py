primeiro = int(input("Digite o primeiro número: "))
ultimo = int(input("Digite o último número: "))

if ultimo < primeiro:
    for i in range(primeiro, ultimo-1, -1):
        print(i)
else:
    for i in range(primeiro, ultimo+1):
        print(i)