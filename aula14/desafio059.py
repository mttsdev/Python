numero = 0
while numero < 1:

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("""
    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")

    opcao_escolhida = int(input("O que deseja fazer? "))
    if opcao_escolhida == 1:
        print("\033[;7m"f"{n1+n2}\033[0;0m")
        deseja_continuar = input("Deseja continuar? ").upper()
        if deseja_continuar == "N":
            print("Saindo do programa...")
            numero += 1
        else:
            numero += 0
    elif opcao_escolhida == 2:
        print("\033[;7m"f"{n1*n2}\033[0;0m")
        deseja_continuar = input("Deseja continuar? ").upper()
        if deseja_continuar == "N":
            print("Saindo do programa...")
            numero += 1
        else:
            numero += 0
    elif opcao_escolhida == 3:
        if n1 > n2:
            print("\033[;7m"f"{n1} é maior\033[0;0m")
            deseja_continuar = input("Deseja continuar? ").upper()
            if deseja_continuar == "N":
                print("Saindo do programa...")
                numero += 1
            else:
                numero += 0
        else:
            print("\033[;7m"f"{n2} é maior\033[0;0m")
            deseja_continuar = input("Deseja continuar? ").upper()
            if deseja_continuar == "N":
                print("Saindo do programa...")
                numero += 1
            else:
                numero += 0
    elif opcao_escolhida == 4:
        numero += 0
    elif opcao_escolhida == 5:
        print("Saindo do programa...")
        numero += 1
    else:
        print("\033[;7m""Opção inválida! Digite novamente\033[0;0m")