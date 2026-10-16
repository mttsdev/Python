valor_pagar = int(input("Digite o valor do produto: "))

while True:
    opcao = int(input("""Escolha a opção de pagamento:
1 - À vista no dinheiro/cheque
2 - No cartão
3 - Até 2x no cartão
4 - 3x ou mais no cartão

"""))
    if opcao == 1:
        print(f"Haverá 10% de desconto no produto:{valor_pagar - valor_pagar * 0.10}")
        break
    elif opcao == 2:
        print(f"Haverá 5% de desconto no produto:{valor_pagar - valor_pagar * 0.05}")
        break
    elif opcao == 3:
        print(f"O valor a ser pago será normal:{valor_pagar}")
        break
    elif opcao == 4:
        print(f"Haverá 20% de juros no produto:{valor_pagar + valor_pagar * 0.20}")
        break
    else:
        print("Opção inválida!")