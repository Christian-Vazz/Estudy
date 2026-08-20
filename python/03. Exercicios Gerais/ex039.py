ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2026 - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em 2026')

if idade < 18:
    print(f'Ainda faltam {18 - idade} ano(s) para o seu alistamento')
    print(f'Seu alistamento será em {ano_nascimento + (18 - idade)}')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {ano_nascimento + 18}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
    