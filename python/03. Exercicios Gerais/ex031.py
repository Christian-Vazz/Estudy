#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem? '))
valor_passagem = distancia * 0.5 if distancia <= 200.0 else distancia * 0.45
print(f'Você está prestes a começar uma viagem de {distancia:.1f}km.')
print(f'O preço da sua passagem será de R${valor_passagem:.2f}')