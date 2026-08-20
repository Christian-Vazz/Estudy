print('Gerador de PA')
print('-=-'*15)

cont = 0
termos = 10

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
atual = primeiro

while True:
    for i in range(0, termos):
        print(f'{atual} -> ', end='')
        atual += razao
        cont += 1
        
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
    
    if termos == 0:
        print(f'Progressão finalizada com {cont} termos mostrados.')
        break