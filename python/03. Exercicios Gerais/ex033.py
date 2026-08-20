valores = []
index = 0
while index <= 2:
    valor_usuario = int(input('Digite um número: '))
    valores.append(valor_usuario)
    index += 1
valores.sort()
print('Maior:', valores[0])
print('Menor:', valores[2])
    