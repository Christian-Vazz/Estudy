from time import sleep
from random import choice

lista = ['Pedra', 'Papel', 'Tesoura']

print('Suas opções:')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')

jogador = int(input('Qual é sua jogada? '))
jogada = lista[jogador].lower()

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-'*10)
jogada_computador = choice(lista).lower()
print(f'Computador jogou {jogada_computador.capitalize()}')
print(f'Jogador jogou {jogada.capitalize()}')
print('-=-'*10)

if jogada_computador == 'pedra':
    
    if jogada == 'pedra':
        print('Empate')
    elif jogada == 'papel':
        print('Jogador Venceu')
    elif jogada == 'tesoura':
        print('Computador Venceu')
    else:
        print('Jogada inválida')

elif jogada_computador == 'papel':
    
    if jogada == 'pedra':
        print('Computador Venceu')
    elif jogada == 'papel':
        print('Empate')
    elif jogada == 'tesoura':
        print('Jogador Venceu')
    else:
        print('Jogada inválida')
    
elif jogada_computador == 'tesoura':    
    
    if jogada == 'pedra':
        print('Jogador Venceu')
    elif jogada == 'papel':
        print('Computador Venceu')
    elif jogada == 'tesoura':
        print('Empate')
    else:
        print('Jogada inválida')
else:
    print('Algo deu errado!')
    
