nome = input('Informe seu nome completo: ').lower().strip().split()
print('Seu primeiro nome é', nome[0].capitalize())
print('Seu último nome é', nome[len(nome) - 1].capitalize())