"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2026 - ano_nascimento
classi = ''
print(f'O atleta tem {idade} anos')

if 2 < idade <= 9:
    classi = 'MIRIM'
elif 9 < idade <= 14:
    classi = 'INFANTIL'
elif 14 < idade <= 19:
    classi = 'JÚNIOR'
elif 19 < idade <= 25:
    classi = 'SÊNIOR'
elif 25 < idade <= 65:
    classi = 'MASTER'
else:
    classi = 'NÃO CLASSIFICADO'

print(f'Classificação: {classi}')

