a = input("Informe o valor A: ")
b = input("Informe o valor B: ")
c = input("Informe o valor C: ")
pi = 3.14159

triangulo = (float(a)*float(c))/2
circulo = float(pi) * (float(c) * float(c))
trapezio = ((float(a) + float(b))*float(c))/2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b) 

print(f"TRIANGULO: {triangulo: .3f}")
print(f"CIRCULO: {circulo: .3f}")
print(f"TRAPEZIO: {trapezio: .3f}")
print(f"QUADRADO: {quadrado: .3f}")
print(f"RETANGULO: {retangulo: .3f}")