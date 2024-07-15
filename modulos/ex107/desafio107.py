import moedas

num = float(input('Digite um preço: RS$'))
print(f'A metade de {num} é {moedas.metade(num)}.')
print(f'O dobro de {num} é {moedas.dobro(num)}.')
print(f'Aumentando 10%, temos {moedas.aumentar(num,10)}.')
print(f'Diminuindo 13%, temos {moedas.diminuir(num,13)}.')