def lerdinheiro(txt=''):
    while True:
        try:
            numero = float(input(txt).replace(',','.'))
            break
        except ValueError:
            print(f'\033[;31mERRO: O dado inserido é um preço inválido!\033[m')
    return numero


def leiaint(msg):
    
    n = ''
    while True:
        n = str(input(msg))
        if n.isnumeric() == False:
            print('\033[0;31mInsira um número inteiro válido!\033[m')
        elif n.isnumeric():
            break
    return int(n)
