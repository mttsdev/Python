valor_do_carro = int(input("Digite a velocidade do carro: "))

if valor_do_carro > 80:
    print(f"MULTADO! pague {(valor_do_carro - 80) * 7.00}")
else:
    print(f"Você cumpriu as leis de trânsito!")