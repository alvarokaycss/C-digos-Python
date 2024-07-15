print('','-'* 35,'\n       SEQUÊNCIA DE FIBONACCI\n','-'*35)
elemento = None
programa = None
while programa != 'FINALIZAR':
    resposta = (input('PARA CONTINUAR DIGITE [CONTINUAR]\nPARA SAIR DIGITE [SAIR]\nINSERIR AQUI:')).strip().upper()
    if resposta == 'CONTINUAR':
        while True:
            try:
                elemento = int(input('QUANTOS TERMOS DEVEM APARECER?'))
                if elemento < 0:
                    print('ERRO! INSIRA NÚMEROS POSITIVOS.')
                    continue
                break
            except ValueError:
                print('ERRO! INSIRA UM NÚMERO VÁLIDO!')
        termo_1 = 0
        termo_2 = 1
        c = 3
        if elemento == 0:
            print(f'NÃO EXISTE UMA SEQUÊNCIA COMPOSTA POR 0 TERMOS.')
        elif elemento == 1:
            print(f'O PRIMEIRO TERMO DA SEQUÊNCIA DE FIBONACCI É {termo_1}.')
        elif elemento == 2:
            print(f'A SEQUÊNCIA É: {termo_1} -> {termo_2}.')
        elif elemento == 3:
            print(f'A SEQUÊNCIA É {termo_1} -> {termo_2} -> {termo_1 + termo_2}.')
        else:
            sequencia = f'A SEQUÊNCIA É: {termo_1} -> {termo_2}' 
            while c <= elemento:
                termo_3 = termo_1 + termo_2
                sequencia += f' -> {termo_3}'
                termo_1 = termo_2
                termo_2 = termo_3
                c += 1
            print(f'{sequencia} -> FIM.')
    elif resposta == 'SAIR':
        programa = 'FINALIZAR'
    else:
        print('DIGITE UMA RESPOSTA VÁLIDA.')
    print('','-'*35)
print('PROGRAMA FINALIZADO.')