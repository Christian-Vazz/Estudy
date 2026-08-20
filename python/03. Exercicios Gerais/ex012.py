valor_produto = float(input('Digite o preço do produto: R$'))
print(f'O produto custava R${valor_produto:.2f} e com desconto de 5% passou a custar R${(valor_produto - (valor_produto * 5 / 100)):.2f}')
