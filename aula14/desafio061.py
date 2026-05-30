p1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 0

while contador < 10:
    conta = contador * razao
    print(f"O {contador+1} termo é: {p1 + conta}")
    contador += 1