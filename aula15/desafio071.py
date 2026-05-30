saque = int(input("Quanto será sacado? "))
cinquenta = 50
vinte = 20
dez = 10
um = 1

while True:
    cedulas_cinquenta = saque / cinquenta
    saque = saque - cinquenta * cedulas_cinquenta
    if (saque / cinquenta) % 2 != 0:
        cedulas_vinte = saque / d

print(f"{cedulas_cinquenta}")