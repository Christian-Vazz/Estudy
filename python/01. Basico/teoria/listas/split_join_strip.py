frase = 'Olha só que, coisa interessante'

lista_de_frases_crua = frase.split(',')

lista_de_frases = []

for i, lista_de_frase in enumerate(lista_de_frases_crua):
    lista_de_frases.append(lista_de_frase.strip())

frase_unida = ' '.join(lista_de_frases)
print(frase_unida)