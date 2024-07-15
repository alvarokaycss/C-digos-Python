def dobro(n, forma=False):
    return n * 2


def metade(n):
    return n / 2


def aumentar(n,p):
   porcent = n * (p/100)
   valor = n + porcent
   return valor


def diminuir(n,p):
    porcent = n * (p/100)
    valor = n - porcent
    return valor


def moedas(preço=0,moeda="R$"):
    forma = f'{moeda}{preço:.2f}'.replace('.',',')
    return forma

