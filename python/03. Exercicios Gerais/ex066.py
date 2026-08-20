qtd_numeros = 0
soma = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    
    if numero == 999:
        break
    qtd_numeros += 1
    soma += numero
print(f'Você digitou {qtd_numeros} numeros e a soma entre eles foi {soma}.')