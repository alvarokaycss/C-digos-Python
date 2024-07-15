soma = 0
lista = []
for c in range(0,6):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        soma += num
    else:
        lista.append(num)
print(f'A soma dos números pares é {soma}.')
print(f'Os números {lista} foram desconsiderados por serem ímpares.')