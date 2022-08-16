name = input("Informe seu nome: ")
salary = input("Informe seu salario: ")
st = input("Informe o total em dinheiro vendido durante o mes: ")

bonus= float(st) * 0.15 + float(salary)

print(f"TOTAL = R$ {bonus: .2f}")