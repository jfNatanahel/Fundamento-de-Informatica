x=int(input("Ingresar los numeros naturales: "))
divisores=1
sumar=0
while divisores<=x:
    if x%divisores==0:
        sumar=sumar+divisores
    divisores=divisores+1
print("La suma de sus divisores: ",sumar)