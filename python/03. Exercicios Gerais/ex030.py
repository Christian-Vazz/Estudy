numero = int(input('\033[0;35mDigite um número:\033[m '))

if numero % 2 == 0:
    print(f'O número {numero} é \033[0;34mPAR\033[m')
else:
    print(f'O número {numero} é \033[0;34mÍMPAR\033[m')
    
