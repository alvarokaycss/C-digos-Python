from datetime import date
ano_atual = date.today().year
lista_maior_idade = []
lista_menor_idade = []
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento:\n'))
    if ano_atual - ano >= 18:
        lista_maior_idade.append(ano)
    else:
        lista_menor_idade.append(ano)
print(f'Nos anos:\n {lista_maior_idade} temos {len(lista_maior_idade)} pessoas maiores de idade.')
print(f'Nos anos:\n {lista_menor_idade} temos {len(lista_menor_idade)} pessoas menores de idade.')
