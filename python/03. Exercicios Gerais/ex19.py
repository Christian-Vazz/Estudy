from random import choice
nomes = []
while True:
    nome = input('Digite um nome: ')
    nomes.append(nome)
    if len(nomes) == 4:
        break
nome = choice(nomes)
print(nomes[nome])