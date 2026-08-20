idades = 0
maior_idade = 0
nome_mais_velho = ''
qtd_mulheres = 0

for qtd in range(1, 5):
    print(f'----- {qtd}° PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower()
        
    idades += idade
    
    if qtd == 1:
        maior_idade = idade
        nome_mais_velho = nome
        
    if idade > maior_idade:
        nome_mais_velho = nome
        maior_idade = idade 
    
    if sexo == 'f' and idade < 20:
        qtd_mulheres += 1
        

media_idade = idades / 4

print(f'A média da idade do grupo é {media_idade:.1f} anos')
print(f'O(a) mais velho(a) tem {maior_idade} anos e se chama {nome_mais_velho}')
print(f'Ao todo são {qtd_mulheres} mulheres com menos de 20 anos')