def par_impar(valor: int = 0) -> str:
    if valor % 2 == 0:
        return f'O valor {valor} é PAR'
    return f'O valor {valor} é IMPAR'
print(par_impar(3))
