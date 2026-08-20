numero = int(input('Digite um número: '))
qtd = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print(f'\033[33m{i}\033[m', end=' ')
        qtd += 1
    else:
        print(f'\033[31m{i}\033[m', end=' ')

primo = 'É PRIMO!' if qtd == 2 else 'NÃO É PRIMO!'

print(f'\nO número {numero} foi dividido {qtd} vezes')
print(f'E por isso ele {primo}')
        