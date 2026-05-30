contador = 1
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-"*30)
    if n < 0:
        print('Programa encerrado')
        break
    else:
        while contador <= 11:
            print(f"{n} x {contador} = {n*contador}")
            contador += 1
            if contador == 11:
                print("-" * 30)
                contador = 1
                break