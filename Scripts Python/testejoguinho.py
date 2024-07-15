from time import sleep
#INTERFACE
print('-='*15)
print('      BANCO SACADIN $.$')
#VARIÁVEIS
saldo = 2000
#PROGRAMA
while True:
    if saldo <= 7000:
        #RESET - CÉDULAS
        cedula_01 = cedula_10 = cedula_20 = cedula_50 = 0
        #INTERFACE
        print('-='*15)
        print('CARREGANDO...!')
        sleep(3.3)
        print('-='*15)
        #ENTRADAS - PROGRAMA
        while True:
            #VERIFICAÇÃO - RESPOSTA
            try:
                resposta = input('O QUE DESEJA FAZER?\nPARA SAQUE PRESSIONE:    [S]\nPARA DEPÓSITO PRESSIONE: [D]\nPARA SAIR PRESSIONE:     [E]\nDIGITE AQUI:').upper().strip() [0]
                break
            except:
                sleep(1)
                print('-='*15)
                print('PROCESSANDO...')
                print('INSIRA UMA RESPOSTA VÁLIDA!')
                print('-='*15)
        print('-='*15)
        #ENTRADAS - OPERAÇÃO - SAQUE
        if resposta == 'S' and resposta != '':
            print('PROCESSANDO INFORMAÇÕES...')
            sleep(2)
            print('VERIFICANDO DADOS...')
            sleep(2)
            print('-='*15)
            print(f'Seu saldo atual é: R${saldo:.2f}.')
            saque = float(input('INSIRA O VALOR DO SAQUE:\n'))
            if saque <= saldo:
                while saque >= 50:
                    saque -= 50
                    saldo -= 50
                    cedula_50 += 1
                while saque >= 20:
                    saque -= 20
                    saldo -= 20
                    cedula_20 += 1
                while saque >= 10:
                    saque -= 10
                    saldo -= 10
                    cedula_10 +=1
                while saque >= 1:
                    saque -=1
                    saldo -=1
                    cedula_01 += 1
                #SAÍDAS - VERIFICAÇÃO - INTERFACE - SAQUE
                print('-='*15)
                print('VERIFICANDO SALDO...')
                sleep(2.5)
                print('PROCESSANDO CÉDULAS...')
                sleep(2.5)
                print('-='*15)
                print('SAQUE REALIZADO! Você recebeu:')
                if cedula_50 > 0:
                    print(f'{cedula_50} Cédulas de RS$50.00.')
                if cedula_20 > 0:
                    print(f'{cedula_20} Cédulas de R$20.00.')
                if cedula_10 > 0:
                    print(f'{cedula_10} Cédulas de R$10.00')
                if cedula_01 > 0:
                    print(f'{cedula_01} Moedas de R$1.00.')
                print(f'Saldo atual: R${saldo:.2f}.')
            else:
                print('-='*15)
                print('VERIFICANDO SALDO...')
                sleep(2.5)
                print('SALDO INSUFICIENTE! TENTE DEPÓSITAR OU AGUARDAR PAGAMENTOS!')
        #ENTRADAS - OPERAÇÃO - DEPÓSITO          
        elif resposta == 'D' and resposta != '':
            print('CARREGANDO OPERAÇÃO...')
            sleep(1.8)
            print('-='*15)
            #VERIFICAÇÃO - RESPOSTA
            while True:
                try:
                    deposito = float(input('VALOR QUE SERÁ DEPÓSITADO:\n'))
                    break
                except:
                    sleep(0.8)
                    print('VALOR INVÁLIDO!')
                    print('-='*15)
            saldo += deposito
            print(f'Saldo atual: R${saldo:.2f}.')
        #SAIR
        elif resposta == 'E' and resposta != '':
            #PLOT TWIST - TEXTO
            texto1 = ('EI!! AQUI É O GERENTE DO BANCO, POR FAVOR NÃO DEPOSITE NADA QUE FAÇA SEU SALDO SUBIR PRA MAIS DE R$7.000,00..').split()
            texto2 = ('PORQUÊ?.. AH, BEM! EU ESTOU TE AVISANDO.. APENAS NÃO FAÇA!').split()
            #PLOT TWIST - SAÍDA
            print('Traceback (most recent call last):')
            print('  File "c:/Users/kaycs/OneDrive/Ambiente de Trabalho/Scripts Python/dindin", all line, in <0010010101>')
            print(' ERROR   ERROR    ERROR ERROR   ERROR')
            print(' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('TerminalError: Someone is hacking into the system.')
            sleep(6)
            for palavra in texto1:
                print(palavra)
                sleep(0.3)
            for palavra in texto2:
                print(palavra)
                sleep(0.8)
            print('BANCO SACADIN $.$ AGRADECE A PREFERÊNCIA!')
            break
        #RESPOSTA - INVÁLIDA
        else:
            print('RESPOSTA INVÁLIDA!')
    elif saldo < 12000:
        print('PROCESSANDO OPERAÇÃO...')
        sleep(3)
        print('ERRO! Operação Cancelada.')
        sleep(4)
        print('\033[2;31;40mnão faça isso!!\033[m')
        break
    elif saldo >= 12000:
        print('Algo está errado..')
        sleep(2)
        print('O gerente do banco tentou te avisar.')
        sleep(1)
        print('Mas mesmo assim você continuou..')
#IDEIAS COLOCAR MÚSICA NA PARTE QUE O GERENTE APARECE
#O QUE VAI ACONTECER SE O SALDO CHEGAR A 10.000?