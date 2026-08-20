print('Gerador de PA')
print('-=-'*15)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
atual = primeiro
cont = 1

while cont <= 10:
    print(f'{atual} -> ', end='')
    atual += razao
    cont += 1
print('FIM')