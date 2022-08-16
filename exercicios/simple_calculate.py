produto1 = input("Insira respectivamente codigo, quantidade e preço unitario do produto: ")

codigo1 , nUnidade1, precoUn1 = produto1.split(' ')

produto2 = input("Insira respectivamente codigo, quantidade e preço unitario do produto 2: ")

codigo2 , nUnidade2, precoUn2 = produto2.split(' ')

valor = int(nUnidade1) * float(precoUn1) + int(nUnidade2) * float(precoUn2)

print(f"VALOR A PAGAR = {valor}")