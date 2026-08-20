total = 0
qtd = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        qtd += 1
        total += i
print(f'A soma dos {qtd} múltiplos foi {total}')