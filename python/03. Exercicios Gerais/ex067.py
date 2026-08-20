while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    
    if tabuada < 0:
        print('Programa Encerrado, volte sempre!')
        break
    
    print('-'*20)
    
    for i in range(0, 11):
        print(f'{tabuada} x {i} = {tabuada * i}')
    
    print('-'*20)