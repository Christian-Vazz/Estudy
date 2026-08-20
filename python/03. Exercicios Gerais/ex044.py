"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""

print('======== Lojas Christian ========')
valor = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
escolha = int(input('Qual sua opção: '))

valor_total = 0

if escolha == 1:
    valor_total = valor - (valor * 10 / 100)
    
elif escolha == 2:
    valor_total = valor - (valor * 5 / 100)
    
elif escolha == 3:
    valor_total = valor
    
elif escolha == 4:
    parcelas = int(input('Quantas parcelas: '))
    valor_total = valor + (valor * 20 / 100)
    valor_parcelas = valor_total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${valor_parcelas:.2f} COM JUROS')

else:
    valor_total = valor
    print('Algo deu errado!')

print(f'Sua compra de R${valor:.2f} vai custar R${valor_total:.2f} no final.')