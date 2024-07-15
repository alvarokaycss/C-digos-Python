from random import randint
from time import sleep
print(' -=-' * 6,'\n        JOKENPÔ\n', '-=- ' * 6 )
while True:
    while True:
        try:
            programa = input('DESEJA CONTINUAR [SIM/NÃO]\n').strip().upper() [0]
            break
        except IndexError:
            print('ERRO! INSIRA ESCOLHA UMA OPÇÃO VÁLIDA')
    if programa == 'S':
        print('ESCOLHA A SUA JOGADA:\n[ 0 ] PEDRA🪨\n[ 1 ] PAPEL🧻\n[ 2 ] TESOURA🔪')
        while True:
            try:
                jogador = int(input('QUAL SUA JOGADA?'))
                if jogador not in [0, 1, 2]:
                    print('ERRO! ESCOLHA UMA OPÇÃO VÁLIDA.')
                else:
                    break
            except ValueError:
                print('ERRO! DIGITE UM NÚMERO VÁLIDO.')
        if jogador == 0:
            jogada_us = 'PEDRA🪨'
        elif jogador == 1:
            jogada_us = 'PAPEL🧻'
        elif jogador == 2:
            jogada_us = 'TESOURA🔪'
        computador = randint(0,2)
        if computador == 0:
            jogada_pc = 'PEDRA🪨'
        elif computador == 1:
            jogada_pc = 'PAPEL🧻'
        elif computador == 2:
            jogada_pc = 'TESOURA🔪'
        if jogador == computador:
            resultado = 'EMPATE!'
        elif computador == 0:
            if jogador == 1:
                resultado = 'JOGADOR VENCEU!'
            elif jogador == 2:
                resultado = 'COMPUTADOR VENCEU!'
        elif computador == 1:
            if jogador == 0:
                resultado = 'COMPUTADOR VENCEU!'
            elif jogador == 2:
                resultado = 'JOGADOR VENCEU!'
        elif computador == 2:
            if jogador == 0:
                resultado = 'JOGADOR VENCEU!'
            elif jogador == 1:
                resultado = 'COMPUTADOR VENCEU!'
        print('JO'), sleep(0.8), print('KEN'), sleep(0.8), print('PÔ!!!'), sleep(0.8)
        print((' -=-' * 6),'\n',f'COMPUTADOR JOGOU: {jogada_pc}\n  JOGADOR JOGOU: {jogada_us}','\n',('-=- ' * 6))
        print(resultado)
    elif programa == 'N':
        break
    else: 
        print('ERRO! INSIRA UMA RESPOSTA VÁLIDA.')    
print('PROGRAMA FINALIZADO!')
