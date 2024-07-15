import moedas

num = float(input('Digite um preço: RS$'))
print(f'A metade de {moedas.moedas(num)} é {moedas.metade(num, True)}.')
print(f'O dobro de {moedas.moedas(num)} é {moedas.dobro(num, True)}.')
print(f'Aumentando 10%, temos {moedas.aumentar(num, 10, True)}.')
print(f'Diminuindo 13%, temos {moedas.diminuir(num, 13, True)}.')
