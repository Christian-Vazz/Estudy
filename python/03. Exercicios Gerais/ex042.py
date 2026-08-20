primeiro = float(input('Informe o primeiro segmento: '))
segundo = float(input('Informe o segundo segmento: '))
terceiro = float(input('Informe o terceito segmento: '))

equilatero = primeiro == segundo and primeiro == terceiro
escaleno = primeiro != segundo and segundo != terceiro and primeiro != terceiro
isosceles = (primeiro == segundo and segundo != terceiro) or (primeiro == terceiro and primeiro != segundo) or (segundo == terceiro and primeiro != terceiro)

tipo_triangulo = ''
triangulo_valido = primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo

if equilatero and triangulo_valido:
    tipo_triangulo = 'EQUILATERO'
elif escaleno and triangulo_valido:
    tipo_triangulo = 'ESCALENO'
elif isosceles and triangulo_valido:
    tipo_triangulo = 'ISOSCELES'
else:
    tipo_triangulo = 'NÃO É TRIÂNGULO'

print(f'Os segmentos acima podem formar um triângulo {tipo_triangulo}')