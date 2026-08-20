from random import randint

print('-=-'*20)
print('VAMOR JOGAR PAR OU ÍMPAR')
print('-=-'*20)

qtd_ganhas = 0

while True:
    valor_usuario = input('Digite um valor: ')
    
    escolha_usuario = input('Par ou Ímpar [P/I]: ').strip().lower().replace('í', 'i')
    
    escolha_usuario_p = escolha_usuario.startswith('p')
    escolha_usuario_i = escolha_usuario.startswith('i') or escolha_usuario.startswith('í')
    
    if not valor_usuario.isdigit():
        print('Valor Inválido!')
        continue
    
    if not (escolha_usuario_p or escolha_usuario_i):
        print('Escolha Inválida!')
        continue
    
    valor_usuario = int(valor_usuario)
    escolha_usuario = escolha_usuario[0]
    
    valor_computador = randint(0, 100)
    soma = valor_usuario + valor_computador
    par_impar = 'p' if soma % 2 == 0 else 'i'
    par_impar_conver = 'PAR' if par_impar == 'p' else 'ÍMPAR'
    
    print('-'*20)
    print(f'Você jogou {valor_usuario} e o computador {valor_computador}. Total de {soma} DEU {par_impar_conver}')
    
    if escolha_usuario == par_impar:
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
        qtd_ganhas += 1
    else:
        print('Você PERDEU!')
        print(f'Você ganhou {qtd_ganhas} vezes')
        break
         
    
    
