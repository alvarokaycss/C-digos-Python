velocidade = int(input('Qual a velocidade do carro?'))
if velocidade > 80:
    multa = 7 * (80 - velocidade) * (-1)
    print(f'Você ultrapassou o limite de velocidade, e será multado em {multa} reais.')
else:
    print('Tudo dentro os conformes, prossiga dentro o limite de velocidade.')