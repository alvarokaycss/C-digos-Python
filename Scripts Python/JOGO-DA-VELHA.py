tabuleiro = [['</>' for c in range(3)] for c in range(3)]
jogador = '<X>'
ato = False

print('-='*15,'\n          JOGO DA VELHA\n','-='*15, '\n LINHAS: [1-2-3] COLUNAS: [1-2-3]\n' ,'-='*15)

while ato == False:
    linha_tab = -1

#IMPRIME O TABULEIRO:    
    for linha in tabuleiro:
        print(*linha, sep=' ')
        
#SOLICITA E VERIFICA AS ENTRADAS:    
    while (linha_tab < 0 or linha_tab > 3):
        try:
            linha_tab = int(input(f'Jogador {jogador}, escolha a LINHA onde deseja marcar [1-3]:'))
            coluna = int(input(f'Jogador {jogador}, escolha a COLUNA onde deseja marcar [1-3]:'))
            if (linha_tab < 0 or linha_tab > 3):
                print('1- Insira posições válidas.')
        except:
            print('2- Insira posições válidas.')
            
#ATUALIZA E VERIFICA O TABULEIRO:
    if tabuleiro[linha_tab-1][coluna-1] == '</>':
        tabuleiro[linha_tab-1][coluna-1] = jogador
    else: #AQUI TROCAMOS O JOGADOR, POIS AO FINAL VAI SER TROCADO DENOVO PEDINDO NOVAMENTE A MESMA TENTATIVA!
        print('Essa posição já está ocupada!')
        jogador = '<O>' if jogador == '<X>' else '<X>'
        
#FAZER VERIFICAÇÃO AQUI:
    ganhador = None
    for c in range(3):
        if (tabuleiro[c][0] == tabuleiro[c][1] == tabuleiro[c][2]) and tabuleiro[c][0] != '</>':
            ganhador = tabuleiro[c][0]
    for c in range(3):
        if (tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c]) and tabuleiro[0][c] != '</>':
            ganhador = tabuleiro[0][c]
            
#VERIFICAÇÃO DA DIAGONAL:            
    if (tabuleiro[0][0] == tabuleiro [1][1] == tabuleiro [2][2]) and tabuleiro[0][0] != '</>':
        ganhador = tabuleiro[0][0]
    if (tabuleiro[2][0] == tabuleiro [1][1] == tabuleiro [0][2]) and tabuleiro[2][0] != '</>':
        ganhador = tabuleiro[2][0]

#VER SE HÁ GANHADOR:
    if ganhador:
        ato = True
        for linha in tabuleiro:
            print(f'{linha}\n')
        print(f'O Jogador {jogador} venceu a partida!')
        
#VERIFICA SE HOUVE EMPATE:
    empate = 0
    for linha in tabuleiro:
        for i in linha:
            if i != '</>':
                empate += 1
                if empate == 9:
                    ato = True
                    for linha in tabuleiro:
                        print(f'{linha}\n')
                    print('O jogo empatou! Tente Novamente.')
        
#TROCA A VEZ DO JOGADOR:        
    jogador = '<O>' if jogador == '<X>' else '<X>'
    
print('Obrigado por jogar!')