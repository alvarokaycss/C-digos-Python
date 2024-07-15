while True: 
    try:
        termo = int(input('PRIMEIRO TERMO:'))
        razao = int(input('RAZÃO:'))
        break
    except ValueError:
        print('ERRO! DIGITE UM NÚMERO VÁLIDO.')
dez = termo + (10 - 1) * razao
p_a = str(termo)
while termo < (dez + razao):
    p_a += f' -> {termo + razao}'
    termo += razao
print(f'{p_a} -> FIM.')
resposta = None
while resposta != 'N':
    dez = termo + (10 - 1) * razao
    resposta = input('DESEJA MAIS TERMOS? [S/N]').strip().upper() [0]
    if resposta == 'S':
        while termo < (dez + razao):
            p_a += f' -> {termo + razao}'
            termo += razao
        print(f'{p_a} -> FIM.')
    if resposta not in ['S','N']:
        print('ERRO! RESPOSTA INVÁLIDA.')
print('PROGRAMA FINALIZADO.')