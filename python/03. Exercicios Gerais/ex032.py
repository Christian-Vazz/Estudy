# Um ano é bissexto se for divisível por 4, com duas exceções: se for divisível por 100, só será bissexto se também for divisível por 400.

from datetime import date

ano = int(input('Informe o ano que deseja analisar (0 para o ano atual): '))
ano_atual = date.today().year
if ano == 0:
    ano = ano_atual
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano é bissexto')
else:
    print('Ano não é bissexto')