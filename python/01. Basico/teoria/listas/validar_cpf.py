"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

while True: 
    resultado_final1 = 0
    resultado_final2 = 0
    multiplicador1 = 10
    multiplicador2 = 11
    resultado1 = 0
    resultado2 = 0
       
    cpf = input('Digite seu cpf: ')
    
    if not len(cpf) == 14:
        print('Quantidade de caracteres inválida')
        continue
    
    if not '.' in cpf or not '-' in cpf:
        print('Digite seu CPF com . e -')
        continue

    cpf_ponto = cpf.split('.')
    cpf_traco = ''.join(cpf_ponto)
    cpf_traco = cpf_traco.split('-')
    cpf_tratado = ''.join(cpf_traco)
    
    for indice in range(len(cpf_tratado) - 2):
        numero_inteiro1 = int(cpf_tratado[indice])
        multiplicacao1 = numero_inteiro1 * multiplicador1
        resultado1 += multiplicacao1
        multiplicador1 -= 1
    
    resultado_final1 = (resultado1 * 10) % 11     
    resultado_final1 = resultado_final1 if resultado_final1 <= 9 else 0
    
    for indice in range(len(cpf_tratado) - 1):
        numero_inteiro2 = int(cpf_tratado[indice])
        resultado2 += numero_inteiro2 * multiplicador2
        multiplicador2 -= 1
    
    resultado_final2 = (resultado2 * 10) % 11
    resultado_final2 = resultado_final2 if resultado_final2 <= 9 else 0
    
    print('Primeiro Digito: ', resultado_final1)
    print('Segundo Digito:', resultado_final2)
        
    
