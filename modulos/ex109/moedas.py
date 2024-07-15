def moedas(preço=0,moeda="R$"):
    forma = f'{moeda}{preço:.2f}'.replace('.',',')
    return forma


def dobro(n, forma=False):
    valor = n * 2
    return valor if valor is False else moedas(valor)


def metade(n, forma=False):
    valor = n / 2
    return valor if valor is False else moedas(valor)


def aumentar(n,p,forma=False):
    porcent = n * (p/100)
    valor = n + porcent
    return valor if valor is False else moedas(valor)
       
       
def diminuir(n,p,forma):
    porcent = n * (p/100)
    valor = n - porcent
    return valor if valor is False else moedas(valor)
