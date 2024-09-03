l = float(input('Quantos metros de largura tem a parede?'))
h = float(input('Quantos metros de altura tem a parede?'))
a = l * h
p = a / 2
print('São {:.2f} metros quadrados, então é necessário {:.2f} litros de tinta.'.format(a,p))
