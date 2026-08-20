from random import randint

nove_digitos = ''
for indice in range(9):
    numero_cast = str(randint(0, 9))
    nove_digitos += numero_cast

resultado_final1 = 0
resultado_final2 = 0
multiplicador1 = 10
multiplicador2 = 11
resultado1 = 0
resultado2 = 0
    
cpf = nove_digitos

# if not len(cpf) == 14:
#     print('Quantidade de caracteres inválida')
    

# if not '.' in cpf or not '-' in cpf:
#     print('Digite seu CPF com . e -')
    

# cpf_ponto = cpf.split('.')
# cpf_traco = ''.join(cpf_ponto)
# cpf_traco = cpf_traco.split('-')
# cpf = ''.join(cpf_traco)

for indice in range(len(cpf) - 2):
    numero_inteiro1 = int(cpf[indice])
    multiplicacao1 = numero_inteiro1 * multiplicador1
    resultado1 += multiplicacao1
    multiplicador1 -= 1

resultado_final1 = (resultado1 * 10) % 11     
resultado_final1 = resultado_final1 if resultado_final1 <= 9 else 0

for indice in range(len(cpf) - 1):
    numero_inteiro2 = int(cpf[indice])
    resultado2 += numero_inteiro2 * multiplicador2
    multiplicador2 -= 1

resultado_final2 = (resultado2 * 10) % 11
resultado_final2 = resultado_final2 if resultado_final2 <= 9 else 0

print(cpf)
print('Primeiro Digito: ', resultado_final1)
print('Segundo Digito:', resultado_final2)

digito_1 = str(resultado_final1)
digito_2 = str(resultado_final2)
cpf_unificado = nove_digitos + digito_1 + digito_2

print(cpf_unificado)