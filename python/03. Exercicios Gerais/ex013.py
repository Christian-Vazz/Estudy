salario = float(input('informe o salário do funcionário: R$'))
reajuste = salario + (salario * 15 / 100)

print(f'O funcionário que ganhava R${salario:.2f}, com aumento de 15%, passou a ganhar R${reajuste:.2f}')