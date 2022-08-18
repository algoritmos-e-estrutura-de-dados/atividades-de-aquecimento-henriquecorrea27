x = input("Informe a distancia em KM percorrida: ")
y = input("Informe o total de combustivel gasto em litros: ")

total = int(x)/float(y)

print(f"{total: .3f} km/l")