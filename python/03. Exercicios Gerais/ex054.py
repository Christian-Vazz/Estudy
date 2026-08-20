from datetime import datetime

data_atual = datetime.now().year
maiores = 0
menores = 0
for qtd in range(1, 8):
    data_pessoa = int(input(f'Em que ano nasceu a {qtd}° pessoa: '))
    
    if data_atual - data_pessoa >= 18:
        maiores += 1
    else:
        menores += 1
    
print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E tivemos {menores} pessoas menores de idade')
        

