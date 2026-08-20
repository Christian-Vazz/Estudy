numero = int(input('Digite um número inteiro: '))
print(
    'Escolha uma das bases para conversão:\n',
    '[ 1 ] Converter para BINÁRIO\n',
    '[ 2 ] Converter para OCTAL\n',
    '[ 3 ] Converter para HEXADECIMAL'
)
escolha = input('Sua opção: ')

match escolha:
    case '1':
        print(f'{numero} convertido para BINÁRIO é {bin(numero)[2:]}')
    case '2':
        print(f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
    case '3':
        print(f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:]}')
