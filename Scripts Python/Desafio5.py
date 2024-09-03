valor_produto = float(input('Qual o valor do produto que deseja receber desconto:'))
desconto = valor_produto * (5 / 100)
produto_desconto = valor_produto - desconto
print(f'Parabéns, você ganhou um desconto de 5%, agora o valor do seu produto é :{produto_desconto}.')
