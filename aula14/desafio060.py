num = int(input("digite um número"))
resultado = 1
contador = 0

while contador < num:
    resultado = resultado * (contador + 1)
    contador += 1
print(resultado)