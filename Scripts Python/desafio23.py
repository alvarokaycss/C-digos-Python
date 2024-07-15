numero = str(input('Digite um número até 4 digitos:'))
numero = ('0000' + numero) [-4:]
print(f'Unidade: {numero[3]}.')
print(f'Dezena: {numero[2]}.')
print(f'Centena: {numero[1]}.')
print(f'Milhar: {numero[0]}.')
print(numero)