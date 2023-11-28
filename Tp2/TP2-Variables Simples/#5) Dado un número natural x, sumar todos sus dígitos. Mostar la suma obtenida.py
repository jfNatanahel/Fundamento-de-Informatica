x=int(input("Ingresar un numero natural: "))
suma=0
while x>0:
    r=x%10
    suma=suma+r
    x=x//10
print("La suma obtenida de sus digitos es: ",suma)