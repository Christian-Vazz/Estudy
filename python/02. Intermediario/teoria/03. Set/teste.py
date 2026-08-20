function = lambda numero: 'par' if numero % 2 == 0 else 'impar'

for i in range(0, 25):
    print(i, function(i))