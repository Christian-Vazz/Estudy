largura = float(input('Digite a largura da parede em m: '))
altura = float(input('Digite a altura da parede em m: '))

area = largura * altura
qtd_tinta = area / 2

print(f'Para pintar uma parede com {area}m² é necessário {qtd_tinta}L de tinta ')