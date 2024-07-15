#Esta variável serve como verificação, onde se uma das operações acontecer se torna True.
#ato = False
#Loop para verificação de entradas.
while True:
    ato = False
    
    try:
        menu = input('Hotel Hotelaria:\n[C] CONTINUAR\n[S] SAIR\nDigite aqui: ').upper().strip() [0]
    except IndexError:
        print('Insira uma opção válida.')
        continue

    if menu == 'C':
#Loop para verificação de entradas.          
        while True:
            try:
                #A necessidade da criação de quartos_tot é devido ao cancelamento de reservas não ultrapassar o limite do hotel.
                quartos_tot = int(input('Informe a quantidade TOTAL de quartos: '))
                quartos_disp = int(input('Informe a quantidade de quartos DISPONÍVEIS: '))
            except ValueError:
                print('Valor inválido.')
                continue
            if quartos_tot >= 0 and quartos_disp <= quartos_tot and quartos_disp >= 0:
                break
            else: 
                print('Não é possível prosseguir com as informações inseridas.')
#Loop para verificação de entradas.
        while True:  
            procedimento = input('QUAL PROCEDIMENTO REALIZAR:\n[R] RESERVA\n[C] CANCELAMENTO\nDigite aqui: ').upper().strip() [0]
        
            if procedimento == 'R':
#Loop para verificação de entradas.
                while True:
                    try:
                        reserva = int(input('Quantos quartos deseja reservar: '))
                    except ValueError:
                        print('Valor inválido.')
                        continue
                    if reserva <= quartos_disp and reserva > 0:
                        quartos_disp -= reserva
                        print(f'Reserva(s) realizada(s) com sucesso!\nQuartos restantes: {quartos_disp}.')
                        ato = True                    
                        break
                    elif reserva > quartos_disp:
                        print(f'Quantidade de quartos indisponíveis para reserva.\nQuantidade de quartos disponíveis: {quartos_disp}.')
                        break #O programa retorna para as opções de procedimento.
                    else:
                        print('Valor inválido.')
                        
            elif procedimento == 'C':
                if quartos_tot != quartos_disp:
                    
#Loop para verificação de entradas.
                    while True:
                        try:
                            cancelamento = int(input('Quantos quartos deseja cancelar a reserva: '))
                        except ValueError:
                            print('Valor inválido.')
                            continue
                        if cancelamento > quartos_tot:
                            print(f'A quantidade de reservas canceladas ultrapassa a quantidade disponível de quartos no hotel ({quartos_tot}).')
                            break #O programa retorna para as opções de procedimento.
                        elif cancelamento <= quartos_tot and cancelamento > 0:
                            quartos_disp += cancelamento
                            print(f'Reserva(s) cancelada(s) com sucesso! Quartos restantes: {quartos_disp}')
                            ato = True
                            break
                        else: 
                            print('Valor inválido.')
                else:
                    print(f'Todos os {quartos_tot} quartos já estão disponíveis.')
                    continue
            else:
                print('Opção Inválida!')
                continue
            
            if ato == True: #Se ato se torna True, então uma das operações foi realizada, voltando ao menu inicial.
                break
            
    elif menu == 'S':
        break
    else:
        print('Insira uma opção válida.')
#PONTOS DE MELHORIA: 1.Função de ver as reservas atuais;
#2. Adicionar o procedimento de "inserir dados", evitando a repetição de inserir a quantidade de quartos toda vez que "Continuar" for executado 
print('Hotel Hotelaria agradece sua preferência!')