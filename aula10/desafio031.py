distancia = int(input("Qual a distância da viagem? "))

if distancia <= 200:
    print(f"A viagem custará {distancia * 0.50}")
else:
    print(f"A viagem custará {distancia * 0.45}")