from math import factorial
num = int(input('DIGITE UM NÚMERO:\n'))
c = num
fatorial = ''
while c > 0:
    fatorial += f'{c}x'
    c -= 1
print(f'{fatorial[:-1]}={factorial(num)}.')
