valor_produto_valido = 0
soma = 0
menor_valor = 1000
produto_mais_de_mil = 0

while True:
    nome_produto = input("Digite o nome do produto: ")
    while valor_produto_valido == 0:
        valor_produto = int(input("Digite o valor do produto: "))
        if valor_produto >= 0:
            valor_produto_valido += 1
            soma += valor_produto
        else:
            print("Valor inválido!")
            valor_produto_valido += 0
    if valor_produto < menor_valor:
        produto_mais_barato = nome_produto
    else:
        pass
    if valor_produto > 1000:
        produto_mais_de_mil += 1

    continuar = input("Deseja continuar? [s] ou [n]: ").lower()
    if continuar == 'n':
        break
    elif continuar == 's':
        valor_produto_valido -= 1
        continue
print(f'Total gasto: {soma}\nProdutos que custam mais de 1000: {produto_mais_de_mil}\nProduto mais barato: {produto_mais_barato}')