termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
decimo = termo + (10 -1) * razao
p_a = str(termo)
while termo < (decimo + razao):
    p_a += f' -> {termo + razao}'
    termo += razao
print(f'{p_a} -> Fim.')