def criar_multiplicador(multiplicador):
    def multiplicar(valor):
        return valor * multiplicador
    return multiplicar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)
quadruplo = criar_multiplicador(4)

numero = 2
numero_dobro = dobro(numero)

print(numero_dobro)