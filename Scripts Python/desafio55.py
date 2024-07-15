lista = []
for pessoa in range(0,5):
    peso = float(input('Digite seu peso:\n'))
    lista.append(peso)
lista.sort()
print(f'O maior peso encontrado é {lista[-1]}')
print(f'O menor peso encontrado é {lista[0]}')