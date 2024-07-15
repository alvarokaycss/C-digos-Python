from time import sleep
for c in range(1, 51):
    if c % 2 == 0:
        print(f'{c} É par.')
    else:
        print(f'{c} É ímpar.')
    sleep(0.5)
print('Sucesso!')
