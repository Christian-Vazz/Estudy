from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')
qtd = 0
numero = randint(0, 10)
while True:
    palpite = int(input('Qual seu palpite? \033[30m'))
    print('\033[0m')
    qtd += 1
    if not 0 <= palpite <= 10:
        continue
    if palpite > numero:
        print('Menos... Tente mais uma vez.')
        continue
    elif palpite < numero:
        print('Mais... Tente mais uma vez.')    
        continue
    else:
        break
print(f'Acertou com {qtd} tentativas. Parabéns!')