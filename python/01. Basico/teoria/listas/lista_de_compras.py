"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

continuar = True
lista = []
while continuar:
    usuario = input("[I]nserir, [A]pagar, [L]istar: ").lower()
    
    if len(usuario) > 1 or len(usuario) < 1:
        print('Quantidade diferente de 1')
        continue
    
    if usuario == 'i':
        inserir = input('Informe o que deseja inserir: ')
        lista.append(inserir)
        print(f'{inserir} inserido na lista')
    
    elif usuario == 'a':
        for index, valor in enumerate(lista):
            print(index, valor)
            
        apagar = input('Escolha o indice que deseja apagar: ')
        
        if apagar.isdigit() and lista:
            apagar = int(apagar)
            if apagar <= len(lista) - 1:  
                item_apagado = lista[apagar]
                del lista[apagar]
                print(f'Apagando item no indice {apagar}, item: {item_apagado}')
            else:
                print('Não é possível apagar, erro de indice')
        else:
            print('Valor inválido para apagar')
    
    elif usuario == 'l':
        print('Listando itens na lista')
        for index, item in enumerate(lista):
            print(index, item)
    else:
        print('Opção inválida')
    