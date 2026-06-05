dias = int(input("Quantos dias? "))
kms = float(input("Quantos kms rodados? "))
preco = dias * 60 + kms * 0.15
print("O total a pagar é de R${:.2f}".format(preco))