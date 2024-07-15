distancia = float(input('Digite distância pecorrida durante a viagem (km):'))
if distancia <= 200:
    print('Valor da passagem: R${:.2f}'.format(0.50 * distancia))
else:
    print('Valor da passagem: R${:.2f}'.format(100 + (0.45 * (distancia - 200))))
print('Obrigado pela preferência!')