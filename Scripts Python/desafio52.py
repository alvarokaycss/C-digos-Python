num = int(input('Digite um número:'))
divisivel = 0
if num > 1:
    for c in range(1, num +1):
        if num % c == 0:
            divisivel += 1
    if divisivel == 2:
        print(f'{num} é um número primo.')
    else:
        print(f'{num} não é um número primo.')
else:
    print(f'{num} não é um número primo.')
    