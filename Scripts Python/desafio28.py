import random
numero_computador = random.randint(0, 5)
numero_usuario = int(input("Tente adivinhar o número que o computador pensou, entre 0 e 5: "))
if numero_usuario == numero_computador:
    print("Parabéns! Você venceu.")
else:
    print("Você perdeu. O número que o computador pensou foi", numero_computador)
    