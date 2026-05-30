soma = 0
while True:
    n = int(input("Digite número: "))
    if n == 999:
        break
    soma+=n
print(f"A soma dentre os valores digitados(exceto o 999) é {soma}")