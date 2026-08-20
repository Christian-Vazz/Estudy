numero = int(input('Digite um número para calcular o fatorial: '))
multi = ''
fatorial = 1
for i in range(numero, 1, -1):
    multi += f'{i} '.replace(' ', ' x ')
    
    fatorial *= i
    
    if i == 2:
        multi += '1'

print(f'Calculando {numero}! = {multi} = {fatorial}')