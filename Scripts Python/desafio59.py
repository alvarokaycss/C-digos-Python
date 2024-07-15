menu = ''
num_1 = None
num_2 = None
while True:
    try:
        print('-' * 20)
        num_1 = float(input('DIGITE UM NÚMERO:\n'))
        num_2 = float(input('DIGITE OUTRO NÚMERO:\n'))
        break
    except ValueError:
        print('ERRO! DIGITE NOVAMENTE NÚMEROS VÁLIDOS.')
while menu != 'sair':
    print('-' * 20)
    print('DIGITAR AÇÃO:\n[1] SOMAR.\n[2] MULTIPLICAR.\n[3] MAIOR NÚMERO.\n[4] NOVOS NÚMEROS.\n[5] SAIR.')
    açao = input('DIGITE A OPERAÇÃO:')
    if açao == '1':
        print(f'RESULTADO: {num_1 + num_2}')
    if açao == '2':
        print(f'RESULTADO: {num_1 * num_2}')
    if açao == '3':
        if num_1 == num_2:
            print('RESULTADO: AMBOS TEM O MESMO VALOR.')
        else:
            print(f'RESULTADO: {max([num_1, num_2])}')
    if açao == '4':
       while True:
        try:
            print('-' * 20)
            num_1 = float(input('DIGITE UM NÚMERO:\n'))
            num_2 = float(input('DIGITE OUTRO NÚMERO:\n'))
            break
        except ValueError:
            print('ERRO! DIGITE NOVAMENTE NÚMEROS VÁLIDOS.')
    if açao == '5':
        menu = 'sair'
    if açao not in ['1', '2', '3', '4', '5']:
        print('ERRO! DIGITE UMA AÇÃO VÁLIDA.')
print('PROGRAMA FINALIZADO!')
