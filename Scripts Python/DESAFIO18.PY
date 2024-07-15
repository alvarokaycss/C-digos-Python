from math import sin , cos , tan , radians
angulo = float(input('Valor do ângulo:'))
angulo_rad = radians(angulo)
seno = sin(angulo_rad)
print('O valor do seno é: {:.2f}.'.format(seno))
cosseno = cos(angulo_rad)
print('O valor do cosseno é: {:.2f}.'.format(cosseno))
tangente = tan(angulo_rad)
print('O valor da tangente é: {:.2f}.'.format(tangente))
#Essa é uma forma alternativa de fazer esse desafio, porém não quer dizer que a sua forma esteja errada!!