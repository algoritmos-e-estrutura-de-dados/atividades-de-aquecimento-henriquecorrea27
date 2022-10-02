a = input("Informe um numero inteiro: ")
b = input("Informe outro numero inteiro: ")
c = input("Informe outro numero inteiro: ")

if  int(a)>int(b) and int(a)>int(c):
    print(f"{a} eh o maior")
elif int(b)>int(a) and int(b)>int(c): 
    print(f"{b} eh o maior")
elif int(c)>int(a) and int(c)>int(b):
    print(f"{c} eh o maior")

    

