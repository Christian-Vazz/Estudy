def multiplicador(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    
    return resultado

valor1 = multiplicador(1.4, 2, 3, 4)
print(valor1) 