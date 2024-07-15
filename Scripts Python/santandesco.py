print('Banco SantanDesco')
saldo = float(input('Valor inicial da conta:'))
if saldo <= 0:
    print('Valor inválido.')
elif saldo >= 1:
    resposta = input('O que você deseja realizar: [SAQUE] ou [DEPOSITO]:').upper()
    if resposta == 'SAQUE':
        saque = float(input('Digite o valor do saque:'))
        if saque <= saldo:
            saldo -= saque
            print(f'Seu saldo é {saldo}.')
        else:
            print('Você não possui saldo suficiente.')
    elif resposta == 'DEPOSITO':
        deposito = float(input('Digite o valor do depósito:'))
        if deposito <= 0:
            print('Valor Inválido')
        elif deposito > 1:
            saldo += deposito
            print(f'Seu saldo é {deposito}.')
    else: 
        print('Operação Inválida.')
print('Banco SantanDesco agradece pela preferência!')