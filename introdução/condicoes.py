import random
n1 = int(input("Tente acertar o número de 0 a 5 que a maquina escolheu \nDigite seu chute:"))
r = random.randint(0,5)
if n1==r:
    print("Parabéns!!")
else:
    print("Você errou")