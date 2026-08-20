valor_casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = float(input('Quantos anos de financiamento: '))

prestacao = valor_casa / (anos * 12)
emprestimo = 'APROVADO' if prestacao <= (salario * 30 / 100) else 'NEGADO'
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')
print('Empréstimo', emprestimo)