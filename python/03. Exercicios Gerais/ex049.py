numero = int(input('Digite um número para mostrar a tabuada: '))
for i in range(0, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')