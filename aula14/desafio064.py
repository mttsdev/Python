numero = 0
total_de_numeros = 0
soma = 0

while numero != 1:
    numero_do_usuario = int(input("digite '999': "))
    if numero_do_usuario == 999:
        numero+=1
        break
    total_de_numeros+=1
    soma+=numero_do_usuario
print(f"você digitou o número 999! Você digitou ao total {total_de_numeros} números e a soma deles é {soma}")