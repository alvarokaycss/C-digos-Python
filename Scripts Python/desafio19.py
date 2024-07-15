import random
nome_1 = input('Digite o nome do 1° aluno:')
nome_2 = input('Digite o nome do 2° aluno:')
nome_3 = input('Digite o nome do 3° aluno:')
nome_4 = input('Digite o nome do 4° aluno:')
lista_nomes = [nome_1, nome_2, nome_3, nome_4]
random.shuffle(lista_nomes)
print(f'A ordem de apresentação é: {lista_nomes}')
