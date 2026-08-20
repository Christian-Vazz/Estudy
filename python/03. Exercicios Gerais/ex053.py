frase = input('Digite uma frase: ').strip().upper()

if ' ' in frase:
    frase = frase.replace(' ', '')

inverso = frase[::-1]

print(inverso)

palindromo = 'Temos um palíndromo!' if frase == inverso else 'Não é um palíndromo!'

print(f'O inverso de {frase} é {inverso}')
print(palindromo)
    
