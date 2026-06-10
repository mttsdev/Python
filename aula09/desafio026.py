frase = input("Digite uma frase: ")
print("Quantidades de 'a' na frase:", frase.count('a'))
print(f"Posição do primeiro 'a': {frase.find('a')+1}")
print(f"Posição do último 'a': {frase.rfind('a')+1}")