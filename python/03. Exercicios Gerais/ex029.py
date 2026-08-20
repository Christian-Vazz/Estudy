"""
    Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7
    print('\033[0;31mMULTADO! Você excedeu o limite permitido que é de 80km/h \033[m')
    print(f'\033[0;31mVocê deve pagar uma multa que é de \033[0;33mR${multa:.2f}\033[m\033[m')

print('\033[0;33mTenha um bom dia! Dirija com cuidado!\033[m')
