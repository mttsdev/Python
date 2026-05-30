# F(n) = F(n-1) + F(n-2)

n = int(input("Digite um número: "))
contador = 0
while contador < n:
    conta = (n-1) + (n-2)
    print(conta)
    contador+=1