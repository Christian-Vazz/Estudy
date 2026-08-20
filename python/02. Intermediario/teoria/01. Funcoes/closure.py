"""
    Higher Order Functions -> Funções de Primeira Classe:
    -> Em Python, as funções são cidadãos de primeira classe, o que significa 
    que podem ser atribuídas a variáveis, passadas como argumentos e 
    retornadas por outras funções, exatamente como números ou strings. 
"""
# Função de primeira classe: atribuída a uma variável
def greet():
    return "Olá"

my_greet = greet  # Atribuição (primeira classe)

# Função de ordem superior: recebe uma função como argumento
def operate(func, name):
    return func() + " " + name

# Usando a função de ordem superior
result = operate(my_greet, "Mundo")
print(result)  # Saída: Olá Mundo   

"""
    Em resumo, todas as funções de ordem superior em Python são também funções de primeira classe, 
    mas nem todas as funções de primeira classe são funções de ordem superior.
"""
