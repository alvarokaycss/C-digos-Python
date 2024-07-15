salario_atual = float(input('Digite o salário atual:'))
aumento = salario_atual * (15/100)
salario_aumento = aumento + salario_atual
print('Você recebeu um aumento de 15%.\nNovo Salário: {:.2f}.'.format(salario_aumento))
