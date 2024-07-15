num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
if num1 <= num2 and num1 <= num3:
    print(f'{num1} é o menor número.')
elif num2 <= num1 and num2 <= num3:
    print(f'{num2} é o menor número:')
else:
    print(f'{num3} é o menor número')
if num1 >= num2 and num1 >= num3:
    print(f'{num1} é o maior número.')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2} é o maior número:')
else:
    print(f'{num3} é o maior número')
#também existe a função sort() que pode ser usada 
#para ordernar uma lista em ordem crescente ou decrescente.