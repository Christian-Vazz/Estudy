from random import randint
from time import sleep

print('\033[0;33m-=-\033[m'*20)
print('\033[0;34mVou pensar em um número de 0 a 5. Tente advinhar...\033[m')
print('\033[0;33m-=-\033[m'*20)

numero_pensado = randint(0, 5)

numero = int(input('Em que número eu pensei? '))

print('Processando...')
sleep(3.0)

if numero == numero_pensado:
    print('\033[0;33mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[0;32mGANHEI! Eu pensei no numero {numero_pensado} e não no {numero}!\033[m')

