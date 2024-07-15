while True:
    print('PROGRAMA DE CONVERSÃO DE NÚMEROS INTEIROS')
    print('DIGITE O NÚMERO A SER CONVERTIDO EM SEGUIDA ESCOLHA A OPÇÃO DESEJADA.')
    print('Digite [1] para BINÁRIO')
    print('Digite [2] para OCTAL')
    print('Digite [3] para HEXADECIMAL')
    num = int(input('Número:'))
    escolha = int(input('Opção:'))
    if escolha == 1:
        print(f'O número {num} convertido para BINÁRIO é:{bin(num) [2:]}.')
    elif escolha == 2:
        print(f'O número {num} convertido para OCTAL é:{oct(num) [2:]}.')
    elif escolha == 3:
        print(f'O número {num} convertido para HEXADECIMAL é:{hex(num) [2:]}.')
    else:
        print('Número ou opção inválida, leia atentamente e utilize o programa conforme orientado.')
    print('Obrigado por utilizar o programa!')
    