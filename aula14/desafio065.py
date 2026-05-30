contador = 0
contador2 = 0
soma = 0
divisao = 0.0
while contador < 1:
    num = int(input("Digite um valor: "))
    soma += num
    while contador2 < 1:
        continuar = input("Deseja continuar? ").lower()
        if continuar == "s":
            break
        elif continuar == "n":
            contador += 1
            break
        else:
            print("Inválido ,tente novamente")
    divisao += 1.0
print(f"A média dos valores é {soma / divisao}")