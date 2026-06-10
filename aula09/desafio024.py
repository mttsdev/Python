nome = input("Em que cidade você nasceu? ")
novo_nome = nome.title().split()
print(f"A cidade digitada começa com 'SANTO'?: {'Santo' in novo_nome[0]}")