x=int(input("Ingresar un numero natural: "))
contador=0
while x>0:
    r=x%10
    contador+=1
    x=x//10
print("La cantidad de digitos que posee es: ",contador)