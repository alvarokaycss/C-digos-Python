print('-' * 5 ,'INTRODUÇÃO A DADOS ESTATÍSTICOS', '-' * 5)
print('''- CONTEÚDO DE TESTE
- NÃO INSERIR VALORES VAZIOS
- PREENCHER TODOS OS DADOS''')
lista_geral = []
lista_media = []
lista_homens = []
lista_mulheres = []
lista_idade_homens = []
lista_idade_mulheres = []
lista_idade_20 = []
feminino = 0
masculino = 0
for c in range(1,5):
    print('-' * 16 , f'{c}°PESSOA' , '-' * 16)
    nome = input('NOME:').upper().strip()
    lista_geral.append(nome)
    idade = int(input('IDADE:'))
    lista_geral.append(idade)
    lista_media.append(idade)
    sexo = input('SEXO[M/F]:').upper()
    lista_geral.append(sexo)
    if sexo == 'M':
        lista_homens.append(nome)
        lista_homens.append(idade)
        lista_idade_homens.append(idade)
        masculino += 1
    elif sexo == 'F':
        lista_mulheres.append(nome)
        lista_mulheres.append(idade)
        lista_idade_mulheres.append(idade)
        feminino += 1
soma = sum(lista_media)
print('-' * 15 , 'RESULTADO' , '-' * 15)
print(f'MÉDIA DAS IDADES DO GRUPO: {soma / 4} ANOS.')
if masculino != 0:
    local_idade_velho = lista_homens.index(max(lista_idade_homens))
    local_nome_velho = local_idade_velho -1
    print(f'HOMEM MAIS VELHO: {lista_homens[local_nome_velho]}.')
else:
    print('NÃO HÁ HOMENS NESSE GRUPO.')
if feminino != 0:
    lista_mulheres_jovens = [valor for valor in lista_idade_mulheres if valor < 20]
    print(f'MULHERES COM IDADE INFERIOR A 20: {len(lista_mulheres_jovens)}.')
else: 
    print(f'NÃO HÁ MULHERES NESSE GRUPO.')
print(f'TODAS AS INFORMAÇÕES DO GRUPO:\n{lista_geral}.')