lista = [1, 2, 3, 4, '1', '2', '3', '4', 2.5]
# O método lista.clear() limpa toda a lista



# Vamos modificar valores na lista para concretizar os assuntos estudados

# Adicionar valores ao final da lista -> lista.append()
print(lista)
valor = input('Digite algo: ')
lista.append(valor)
print(lista)

# Removendo valores com indice -> del lista[indice]
del lista[0]
print(lista)

# Removendo valor ao final ou com indice e retornando o valor removido -> lista.pop() ou lista.pop(indice)
valor_removido = lista.pop(1)
print(lista)

# Adicionando valor em um indice escolhido -> lista.insert(indice, valor)
lista.insert(0, 50)
print(lista)

# Extendo listas com extend e + ->
lista_a = [1, 2, 3] 
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)
lista_d = lista_a
print(lista_d)

# Copiando valores de uma lista para outra lista
# Pois quando temos dados mutaveis, uma variavel lista_b aponta para o mesmo valor na memoria
# de uma lista_a

lista_a = [1, 2, 3, 4]
lista_b = lista_a.copy() # Dessa forma o valor é copiado e um não interfere no outro
print(lista_a)

print(lista_b)