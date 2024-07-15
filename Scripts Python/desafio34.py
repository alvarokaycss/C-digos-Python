salario = float(input(f'Digite o valor do seu sálario:'))
if salario > 1250: 
    salario = salario + (salario * (10/100))
    print(f'Seu salário atual agora é: {salario:.2f}')
else: 
    salario = salario + (salario * (15/100))
    print(f'Seu salário atual agora é: {salario:.2f}')
print('Trabalho feito, salário feito, vote 4020 o seu prefeito!')
