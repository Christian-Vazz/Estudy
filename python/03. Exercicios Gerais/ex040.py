# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media}')
if 0 <= media < 5:
    print('Aluno REPROVADO!')
elif 5 <= media < 7:
    print('Aluno em RECUPERAÇÃO')
elif 7 <= media <= 10:
    print('Aluno APROVADO')
else:
    print('Média INVÁLIDA')