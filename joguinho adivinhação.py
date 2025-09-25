import random

numero_aleatorio = random.randint(1, 100)
acertou_palpite = False
tentativas = 6


while acertou_palpite == False and tentativas > 0 and tentativas <= 6:
    palpite = int(input("Insira seu palpite: "))
    if palpite == numero_aleatorio:
        print("Parabéns, você acertou!")
        acertou_palpite = True
    elif palpite > numero_aleatorio:
        tentativas = tentativas - 1
        print(f"Seu palpite é muito alto, você ainda tem {tentativas} tentativas restantes, tente novamente")
    else:
        tentativas = tentativas - 1
        print(f"Seu palpite é muito baixo, você ainda tem {tentativas} tentativas restantes, tente novamente")

