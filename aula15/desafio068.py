import random


soma = 0
vitorias_consecutivas = 0

while True:
    numero_do_computador = random.randint(0, 10)
    par_ou_impar = int(input("qual você escolhe? \n [1] Par \n [2] Ímpar \n"))
    if par_ou_impar == 1:
        print("Par Escolhido")
        palpite = int(input("Digite um número: "))
        soma += palpite + numero_do_computador
        if soma % 2 == 0:
            print(f"Número do computador: {numero_do_computador}")
            print("Parabéns! Você ganhou!")
            vitorias_consecutivas += 1
            print(f"Vitórias consecutivas: {vitorias_consecutivas}")
        else:
            print(f"Número do computador: {numero_do_computador}")
            print(f"Você perdeu! vitorias consecutivas: {vitorias_consecutivas}")
            break
    elif par_ou_impar == 2:
        print("Ímpar Escolhido")
        palpite = int(input("Digite um número: "))
        soma += palpite + numero_do_computador
        if soma % 2 == 1:
            print(f"Número do computador: {numero_do_computador}")
            print("Parabéns! Você ganhou!")
            vitorias_consecutivas += 1
            print(f"Vitórias consecutivas: {vitorias_consecutivas}")
        else:
            print(f"Número do computador: {numero_do_computador}")
            print(f"Você perdeu! vitorias consecutivas: {vitorias_consecutivas}")
            break