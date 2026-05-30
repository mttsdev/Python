p1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 0
nova_pa = 10
while contador < nova_pa:
    conta = contador * razao
    print(f"O {contador+1} termo é: {p1 + conta}")
    contador += 1
    if contador == nova_pa:
        continuar = input("Deseja continuar? ").upper()
        if continuar == "S":
            novo_p1 = int(input("mais quantos termos? "))
            nova_pa += novo_p1
        else:
            pass