dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = dinheiro / 5.11
print("Com {} você pode comprar US${:.2f}".format(dinheiro, dolar))