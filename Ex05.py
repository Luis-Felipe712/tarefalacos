candidatos = ['Jair Rodrigues', 'Carlos Luz', 'Neves Rocha', 'Nulo', 'Branco']
votos = [0] * 5

while True:
    print('As opções são:')
    print('1. Candidato Jair Rodrigues')
    print('2. Candidato Carlos Luz')
    print('3. Candidato Neves Rocha')
    print('4. Nulo')
    print('5. Branco')
    print('Entre com o seu voto:')
    
    opcao = int(input())
    if opcao == 6:
        break
    elif opcao >= 1 and opcao <= 5:
        votos[opcao-1] += 1
    else:
        print('Opção inválida. Tente novamente.')

total_votos = sum(votos)
porcentagem_nulos = votos[3] / total_votos * 100
porcentagem_brancos = votos[4] / total_votos * 100

print('Resultado final:')
for i in range(5):
    print(f'{candidatos[i]}: {votos[i]} votos ({votos[i]/total_votos*100:.2f}%)')
print(f'Porcentagem de votos nulos: {porcentagem_nulos:.2f}%')
print(f'Porcentagem de votos brancos: {porcentagem_brancos:.2f}%')

if votos[0] > votos[1] and votos[0] > votos[2]:
    print('Candidato Jair Rodrigues venceu a eleição.')
elif votos[1] > votos[0] and votos[1] > votos[2]:
    print('Candidato Carlos Luz venceu a eleição.')
elif votos[2] > votos[0] and votos[2] > votos[1]:
    print('Candidato Neves Rocha venceu a eleição.')
else:
    print('A eleição terminou empatada.')