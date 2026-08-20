perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 x 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

qtd_acertos = 0

for pergunta in perguntas:
    
    print('Pergunta: ', pergunta)
    
    for i, option in enumerate(perguntas['Opções']):
        print(f'{i}) {option}')
    
    escolha = input('Escolha uma opção: ')
    
    if not escolha.isdigit():
        print('Errou!!')
        continue
    
    escolha_int = int(escolha)
    
    if not 0 <= escolha_int < len(pergunta['Opções']):
        print('Erro!!')
        continue
    
    print('Acertou!!')
    qtd_acertos += 1

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas')