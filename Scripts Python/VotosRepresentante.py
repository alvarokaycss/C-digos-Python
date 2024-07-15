#Variáveis utilizadas dentro do programa e suas respectivas mensagens.
candidatos = [['Laizy', 0], ['Victor', 0], ['Gerferson', 0]]
votos_tot = list()
num_votantes = int(input('Quantas pessoas irão votar:' ))
mensagem_confirme = 'escolhido(a), CONFIRME seu VOTO.\nCONFIRMAR [C]\nVOLTAR [V]\nDigite aqui: '
mensagem_retorno = 'Atenção! Retornando a seleção de candidatos.'
mensagem_voto = 'Voto registrado!\nPRÓXIMO ELEITOR.'

print(f'Candidatos a eleição: {candidatos[0][0]} [1], {candidatos[1][0]} [2], {candidatos[2][0]} [3].')
#Loop para contabilização de votos.
while num_votantes != 0:
    
    candidato = int(input('SELECIONE seu candidato, conforme o número AO LADO do NOME.'))

#Confome a escolha do usuário o sistema irá contabilizar o voto ao lado do nome do candidato e emitir a saída conforme a opreção realizada.
    
    if candidato == 1:
        confirmar = input(f'{(candidatos[0][0]).upper()}, {mensagem_confirme}').upper().strip() [0]
        if confirmar == 'C':
            candidatos[0][1] += 1
            num_votantes -= 1
            print(mensagem_voto)
        elif confirmar == 'V':
            print(mensagem_retorno)
            
    elif candidato == 2:
        confirmar = input(f'{(candidatos[1][0]).upper()}, {mensagem_confirme}').upper().strip() [0]
        if confirmar == 'C':
            candidatos[1][1] += 1
            num_votantes -= 1
            print(mensagem_voto)
        elif confirmar == 'V':
            print(mensagem_retorno)
    
    elif candidato == 3:
        confirmar = input(f'{(candidatos[2][0]).upper()}, {mensagem_confirme}').upper().strip() [0]
        if confirmar == 'C':
            candidatos[2][1] += 1
            print(mensagem_voto)
            num_votantes -= 1
        elif confirmar == 'V':
            print(mensagem_retorno)
            
#Loop para verificação de votos.
for candid in candidatos:
    votos_tot.append(candid[1])
#Loop para encontrar e emitir o vencedor conforme o número de votos. Note que não há critério de empate.
for candid in range(0,len(candidatos)):
    if candidatos[candid][1] == max(votos_tot):
        print(f'{candidatos[candid][0]} FOI O(A) VENCEDOR(A) DA ELEICÃO!')
#Neste código não foi incluído sistemas de verificações mais "sofisticados", além do que se pede.
print(f'LISTA COMPLETA COM CANDIDATOS E SEUS VOTOS, RESPECTIVAMENTE:\n{candidatos}.')