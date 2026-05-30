maior_de_idade = 0
homens = 0
mulheres_menos_de_vinte = 0
idade_valida = 0
sexo_valido = 0

while True:
    while idade_valida == 0:
        idade = int(input("Digite sua idade: "))
        if idade >= 0 and idade <= 105:
            idade_valida += 1
        else:
            print("Idade inválida!")
            idade_valida += 0
    while sexo_valido == 0:
        sexo = input("Digite seu sexo [F] ou [M]: ").upper()
        if sexo == 'M' or sexo == 'F':
            sexo_valido += 1
        else:
            print("Sexo inválido!")
            sexo_valido += 0
    if idade >= 18:
        maior_de_idade += 1
    else:
        maior_de_idade += 0
    if sexo == "M":
        homens += 1
    else:
        homens += 0
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_vinte += 1
    else:
        mulheres_menos_de_vinte += 0
    continuar = input("Deseja continuar? [S] ou [N]: ").upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
print(f"Maiores de Idade: {maior_de_idade}\nHomens: {homens}\nMulheres menos de vinte anos: {mulheres_menos_de_vinte}")