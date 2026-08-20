dias = int(input('Quantos dias alugado: '))
quilometros = float(input('Quantos quilometros foram rodados: '))
pagamento = (60 * dias) + (0.15 * quilometros)

print(f'Total a pagar pelo aluguel é R${pagamento:.2f}')