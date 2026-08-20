string = input('Digite uma frase: ').lower()
print('A letra A apareve {} vezes'.format(string.count('a')))
print('A letra A aparece primeiro na posição {}'.format(string.find('a')+1))
print('A letra A aparece por último na posição {}'.format(string.rfind('a')+1))