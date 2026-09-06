num1 = int(input("Digite o primeira reta: "))
num2 = int(input("Digite o segunda reta: "))
num3 = int(input("Digite o terceira reta: "))

if num1 + num2 > num3 and num1 + num3  > num2 and num2 + num3 > num1:
    print(f"As três retas formam um triângulo")
else:
    print(f"As três retas NÃO formam um triângulo")