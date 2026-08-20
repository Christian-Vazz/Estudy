print('-=-'*15)
print('Analisador de Triângulos')
print('-=-'*15)
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

triangulo = (c < a + b) and (b < a + c) and (a < b + c)
condicao = 'PODEM FORMAR' if triangulo else 'NÃO PODEM FORMAR'

print(f'Os segmentos {condicao} triângulo!')