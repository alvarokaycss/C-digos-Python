from math import ceil
casa = float(input('Valor da casa:'))
salario = float(input('Salário do comprador:'))
anos = int(input('Quantidade de anos que deseja ser parcelado:'))
valor_mensal = ceil(casa / (anos * 12))
if valor_mensal < 0.3 * salario:
    print(f'''O valor a ser pago mensalmente é R${valor_mensal:.2f}
\033[1;30;46mFinanciamento realizado com sucesso!\033[m''')
elif valor_mensal == 0.3 * salario:
    print(f'''O valor a ser pago mensalmente é R${valor_mensal:.2f}.
\033[1;30;46mFinanciamento no limite, porém realizado!\033[m''')
elif valor_mensal > 0.3 * salario:
    print('\033[0;31;40mFINANCIAMENTO NEGADO!\nParcelamento excedeu o limite salarial de 30%.\033[m')