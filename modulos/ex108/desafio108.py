import moedas

num = float(input('Digite um preço: RS$'))
print(f'A metade de {moedas.moedas(num)} é {moedas.moedas(moedas.metade(num))}.')
print(f'O dobro de {moedas.moedas(num)} é {moedas.moedas(moedas.dobro(num))}.')
print(f'Aumentando 10%, temos {moedas.moedas(moedas.aumentar(num,10))}.')
print(f'Diminuindo 13%, temos {moedas.moedas(moedas.diminuir(num,13))}.')
