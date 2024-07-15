nome = str(input('Digite o seu nome:'))
print(f'Nome em MAIÚSCULO: {nome.upper()}.')
print(f'Nome em minúsculo: {nome.lower()}.')
nome_sem_espaço = nome.replace(' ' ,'')
print(f'Quantidade de letras: {len(nome_sem_espaço)}.')
primeiro_nome , segundo_nome , terceiro_nome = nome.split()[:3]
quantidade = primeiro_nome + segundo_nome + terceiro_nome
print(f'Quantidade de letras no primeiro nome {len(primeiro_nome)}')
print(f'Quantidade de letras do primeiro, segundo e terceiro nome: {len(quantidade)}.')
#Outra maneira de fazer seria:
#nome = str(input('Digite seu nome completo:')).strip()
#print(f'Seu nome em letras maiúsculas é: {nome.upper()}.')
#print(f'Seu nome em letras minúsculas é: {nome.lower()}.')
#print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.')
#print(f'Seu primeiro nome tem {nome.find(' ')} letras.')