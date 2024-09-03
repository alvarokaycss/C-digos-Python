from math import pow, sqrt
cateto_1 = float(input('Digite o valor do comprimento do cateto um:'))
cateto_2 = float(input('Digite o valor do comprimento do cateto dois:'))
hipotenusa = sqrt(pow(cateto_1,2) + pow(cateto_2,2))
print(f'A hipotenusa desse triângulo é:{hipotenusa}')
