import math

co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))

h = pow(co, 2) + pow(ca, 2)
hipotenusa = math.sqrt(h)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))