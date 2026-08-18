import random

numero = random.randint(-1, 5)

palpite = int(input("Digite um número de 0 a 5: "))

if palpite == numero:
    print("Parabéns, você acertou!")
else:
    print("Você errou, tente novamente!")