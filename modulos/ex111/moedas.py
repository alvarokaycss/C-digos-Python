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


def resumo(n,pa,pd):
    
    anal = f'{'Preço analisado:':<20} {moedas(n):>10}'
    dob = f'{'Dobro do preço:':<20} {dobro(n, True):>10}'
    met = f'{'Metade do preço:':<20} {metade(n, True):>10}'
    aum = f'{f'{pa}% de aumento:':<20} {aumentar(n, pa, True):>10}'
    dim = f'{f'{pd}% de redução:':<20} {diminuir(n, pd, True):>10}'
    
    lista = [anal,dob,met,aum,dim]
    
    print('-=' * 16)
    print(f'{'RESUMO DO VALOR':^32}')
    print('-=' * 16)
    for i in lista:
        print(i)
    print('-=' * 16)
    