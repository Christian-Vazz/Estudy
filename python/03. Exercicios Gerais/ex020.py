from random import shuffle
itens = []

while True:
    item = input('Digite algo: ')
    itens.append(item)
    if len(itens) == 4:
        break
shuffle(itens)
print(itens)
