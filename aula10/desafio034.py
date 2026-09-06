salario = int(input("Digite o seu salário: "))

if salario > 1250.00:
    print(f"Seu salário com o aumento de 10% será: {salario + salario * 10/100}")
else:
    print(f"Seu salário com o aumento de 15% será: {salario + salario * 15 / 100}")