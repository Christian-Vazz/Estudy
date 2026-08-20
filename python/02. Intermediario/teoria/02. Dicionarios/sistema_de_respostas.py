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

acertos = 0

for i in range(0, len(perguntas)):
    
    print(f'Pergunta: {perguntas[i]["Pergunta"]}')
    
    for j, options in enumerate(perguntas[i]['Opções']):
        print(f'{j}) {options}')
    
    escolha = input('Escolha uma opção: ')
    
    if not escolha.isdigit():
        print('Errou!!')
        continue
    
    
    escolha = int(escolha)

    if not 0 <= escolha < len(perguntas[i]['Opções']):
        continue
    
    if not perguntas[i]['Opções'][escolha] == perguntas[i]['Resposta']:
        print('Errou!!')
        continue
    
    acertos += 1
    print('Acertou!!')

print(f'Você acertou {acertos} de {len(perguntas)} perguntas')