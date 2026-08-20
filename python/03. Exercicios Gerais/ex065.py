soma = qtd_numeros = 0

maior = 0
menor = 0

while True:
    numero = input('Digite um número: ')
    
    if numero.isdigit() != True:
        print('Valor inválido, digite novamente!')
        continue
    
    numero = int(numero)
    
    qtd_numeros += 1
    soma += numero
    
    if qtd_numeros == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero  
    elif numero < menor:
        menor = numero
    else:
        pass
    
    continuar = input('Deseja continuar? [S/N] ').lower()

    if continuar == 's':
        continue
    else:
        break
media = soma / qtd_numeros
print(f'Você digitou {qtd_numeros} números e a média é {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')


