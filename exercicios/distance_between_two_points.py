p1 = input("Insira respectivamente x1 e y1: ")

x1, y1 = p1.split(' ')

p2 = input("Insira respectivamente x2 e y2: ")

x2, y2 = p2.split(' ')

num = ((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2)

distance = float(num)**0.5

print(f"{distance: .4f}")

