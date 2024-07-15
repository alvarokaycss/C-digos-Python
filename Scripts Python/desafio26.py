frase = str(input('Digite uma frase:'))
qntd_letras_a = frase.lower().count('a')
print(f'Essa frase contém {qntd_letras_a} letras "a".')
primeira_vez = frase.lower().replace(' ' , '').find('a') + 1
print(f'Ela aparece na primeira posição: {primeira_vez}.')
ultima_vez = frase.lower().replace(' ' , '').rfind('a') + 1
print(f'Ela aparece na ultima posição: {ultima_vez}.')
