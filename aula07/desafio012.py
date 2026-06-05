dinheiro = float(input("Qual é o preço do produto? R$"))
print("O produto que custava R${}, na promoção de 5% vai custar R${:.2f}.".format(dinheiro, dinheiro - dinheiro * (5/100)))