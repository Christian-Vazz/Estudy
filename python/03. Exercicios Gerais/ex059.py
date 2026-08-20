from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

while True:
    
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do programa')
    
    option = input('Qual é sua opção? ')
    
    if option == '1':
        soma = valor1 + valor2
        print(f'A soma de {valor1} + {valor2} = {soma}')
        print('-=-' * 15)
    
    elif option == '2':
        multi = valor1 * valor2
        print(f'O resultado de {valor1} x {valor2} = {valor1 * valor2}')
        print('-=-' * 15)
    
    elif option == '3':
        if valor1 > valor2:
            print(f'Entre {valor1} e {valor2} o maior valor é {valor1}')
            print('-=-' * 15)
        elif valor2 > valor1:
            print(f'Entre {valor1} e {valor2} o maior valor é {valor2}')
            print('-=-' * 15)
        else:
            print(f'{valor1} = {valor2}')
            print('-=-' * 15)
        
    elif option == '4':
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    
    elif option == '5':
        print('Finalizando...')
        print('-=-' * 15)
        sleep(3.0)
        break

    else:
        print('Opção inválida!!')
    
print('Fim do programa! Volte sempre!')
print('-=-' * 15)
    
    
    
    
    
    