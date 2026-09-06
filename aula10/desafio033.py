num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"O número {num1} é o maior de todos")

else:
    if num1 < num2:
        if num1 < num3:
            print(f"O número {num1} é o menor de todos")

if num2 > num1 and num2 > num3:
    print(f"O número {num1} é o maior de todos")

else:
    if num2 < num1:
        if num2 < num3:
            print(f"O número {num2} é o menor de todos")

if num3 > num1 and num3 > num2:
    print(f"O número {num3} é o maior de todos")

else:
    if num3 < num1:
        if num3 < num2:
            print(f"O número {num3} é o menor de todos")