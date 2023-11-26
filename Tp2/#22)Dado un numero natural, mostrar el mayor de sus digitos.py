x=int(input("Ingresar un numero natural: "))
m=0
while x>0:
    r=x%10
    if r>m:
        m=r
    x=x//10
print("El mayor de sus digitos es: ",m)