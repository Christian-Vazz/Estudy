# An = A1 + (N - 1)*r

print('='*30)
print('10 Termos de uma P.A'.ljust(5, ' '))
print('='*30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

ultimo = primeiro + (10 - 1) * razao

for i in range(primeiro, ultimo + razao, razao):
    print(i, end=' → ')

print('Acabou!')