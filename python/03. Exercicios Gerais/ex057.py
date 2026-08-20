sexo = input('Informe seu sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MF':
    sexo = input('Dados Inválidos. Por favor, digite seu sexo novamente: ')
print(f'Sexo {sexo} registrado com sucesso!')