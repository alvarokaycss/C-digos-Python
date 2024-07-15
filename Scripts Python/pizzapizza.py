#Variáveis
total_pizza = total_dia = verificador = 0
#Entradas e verificações:
while verificador != 3:
    print('-=' *10)
    pedido = input('Qual pizza você deseja?\n[CALABRESA: R$25]\n[MANJERICÃO: R$25]\n[PEPPERONI: R$35]\n[PULAR]\nDIGITE AQUI:').upper().strip()
    print('-=' *10)
    if pedido == 'PULAR':
        verificador += 1
        print('Registrado.')
        continue
    elif pedido == 'CALABRESA' or pedido == 'MANJERICÃO':
        total_pizza += 1
        total_dia += 25
        verificador += 1
        print('Registrado.')
    elif pedido == 'PEPPERONI':
        total_pizza += 1
        total_dia += 35
        verificador += 1
        print('Registrado.')
    else:
        print('Opção Inválida.')
    print('-=' *10)
    adicional = input('Deseja adicionar borda? Valor adicional de R$2.00.\n[CATUPIRY]\n[CHEDDAR]\n[PULAR]\nDIGITE AQUI:').upper().strip()
    if adicional == 'CATUPIRY' or adicional == 'CHEDDAR':
        total_dia += 2
    elif adicional == 'PULAR':
        None
    print('-=' *10)
    entrega = input('Seu pedido é para viagem? Valor adicional de R$5.00.\n[VIAGEM]\n[PULAR]\nDIGITE AQUI:').upper().strip()
    if entrega == 'VIAGEM':
        total_dia += 5
    elif entrega == 'PULAR':
        None
#Saídas
print('-=' *10)
print(f'Pizzaria PizzaPizza agradece a preferência!\nTotal de vendas: {total_pizza}.\nValor total de vendas: R${total_dia:.2f}.')
print('-=' *10)
